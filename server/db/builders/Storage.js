r = require('rethinkdb');

var db = db || {};

db = {
  connection : null,
  host : 'localhost',
  post : 28015,
  names : {
    test : 'test'
  },
  tables : {
    users : 'users',
    authors : 'authors',
    reviews : 'reviews'
  },
  data : {
    users : [
      { name: "Barış Güler", age : 30 },
      { name: "Laçin İrem Salgırtay", age : 33 },
      { name: "Bahar Güler", age : 27 }
    ],
    reviews : [ 
      { user_id : "1", start : 3, optional_comment : "Everything was fine but a bit late" },
      { user_id : "2", start : 4, optional_comment : "thank you for that delicious meal!" },
      { user_id : "3", start : 5, optional_comment : "Perfection." }
    ]
  }
}

var Storage = (function () {

  function connect (db, callback) {
    r.connect( {host: db.host, port: db.port}, function(err, conn) {
      if (err) throw err;
      db.connection = conn;
      callback(true);
    });
  };

  function createTable (tableName, callback) {
    r.db(db.names.test).tableCreate(tableName).run(db.connection, function(err, result) {
        if (err) throw err;
        console.log(JSON.stringify(result, null, 2));
        callback(true);
    })
  }

  function makeStartupQuery (callback) {
    connect(db, function (succeed) {
      r.db(db.names.test).table(db.tables.users).insert(db.data.users).run(db.connection, function(err, result) {
        if (err) throw err;
        console.log(JSON.stringify(result, null, 2));
        callback(true);
      })
    });
  };

  function createReviewsData (tableName, callback) {
    connect(db, function (succeed) {
      r.db(db.names.test).table(db.tables.reviews).insert(db.data.reviews).run(db.connection, function(err, result) {
        if (err) throw err;
        console.log(JSON.stringify(result, null, 2));
      })
    });
  }

  function init () {  
    connect(db, function (connected) {
      if (!connected) throw 'Error occured.';
      /*
      createTable(db.tables.reviews, function (tableCreated) {
        if (!tableCreated) throw new Error('Error during table creating.');
      */
        makeStartupQuery(function (succeed) {
          if (!succeed) throw new Error('Error occured.');
          console.log('Database query is successfull.' + Date.now());
          createReviewsData('reviews', function (succeed) {
            if (!succeed) throw new Error('Error occured.');
            console.log('Database query is successfull.' + Date.now());
          })
        })
      /*})*/
    })
  }

  return {
    init : init
  }

})();

Storage.init();