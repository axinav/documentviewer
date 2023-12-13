from PySide6.QtSql import QSqlDatabase, QSqlDriver, QSqlQuery
class Project:
    def __init__(self,projectName=':memory:') -> None:
        self.dbName = projectName
        self.connect()

    def connect(self):
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName(self.dbName)
        con.open()
        self.createTables()

    def createTables(self):
        query = QSqlQuery()
        res =query.exec(
            """CREATE TABLE IF NOT EXISTS subjects
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            casetype TEXT
            )"""
        )
        query.exec(
            """CREATE TABLE IF NOT EXISTS objects
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            objtype TEXT NOT NULL,
            kn TEXT,
            address TEXT,
            subject_id INTEGER,
            FOREIGN KEY (subject_id) REFERENCES subjects (id)
            ON DELETE CASCADE
            )"""
        )
        query.exec(
            """CREATE TABLE IF NOT EXISTS documents
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctype TEXT NOT NULL,
            subtype TEXT,
            name TEXT,
            number TEXT,
            data TEXT,
            author TEXT,
            object_id INTEGER,
            FOREIGN KEY (object_id) REFERENCES objects (id)
            ON DELETE CASCADE
            )"""
        )
        query.exec(
            """CREATE TABLE IF NOT EXISTS images
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT NOT NULL,
            page INTEGER,
            doc_id INTEGER,
            FOREIGN KEY (doc_id) REFERENCES documents (id)
            ON DELETE CASCADE
            )"""
        )
    def insertSubject(self,name,casetype):
        query = QSqlQuery()
        query.prepare("INSERT INTO subjects (name, casetype) "
            "VALUES (:name, :casetype) ")
        query.bindValue(":name", name)
        query.bindValue(":casetype", casetype)
        query.exec()
        return query.lastInsertId()

    def selectSubjects4Model(self):
        query = QSqlQuery()
        query.exec("""SELECT id, name ||', '||casetype FROM subjects""")
        return query
        
    def insertObject(self,
        objtype, kn, address, subject_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO objects (objtype, kn, address, subject_id) "
                     "VALUES ( :objtype, :kn, :address, :subject_id) ")
        query.bindValue(":objtype", objtype)
        query.bindValue(":kn",kn)
        query.bindValue(":address", address)
        query.bindValue(":subject_id", subject_id)
        query.exec()
        return query.lastInsertId()

    def selectObjects4Model(self):
        query = QSqlQuery()
        query.exec("""SELECT id, objtype || ' KN' || kn || ' ' || address FROM objects""")
        return query

    def insertDocument(self, doctype , subtype,  name,  number,  data,  author,  object_id): 
        query = QSqlQuery()
        query.prepare("INSERT INTO documents (doctype , subtype,  name,  number,  data,  author,  object_id) "
        "VALUES (:doctype, :subtype, :name, :number, :data, :author, :object_id) ")
        query.bindValue(":doctype", doctype) 
        query.bindValue(":subtype", subtype)
        query.bindValue(":name", name)
        query.bindValue(":number", number)
        query.bindValue(":data", data)
        query.bindValue(":author", author)
        query.bindValue(":object_id", object_id)
        query.exec()
        return query.lastInsertId()

    def insertImage(self,path, page, doc_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO images (path, page, doc_id) "
            "VALUES (:path, :page, :doc_id) ")
        query.bindValue(":path",path)
        query.bindValue(":page", page)
        query.bindValue(":doc_id", doc_id)
        query.exec()
        return query.lastInsertId()
if __name__ == "__main__":
    project = Project()
    project.insertSubject('ist','ist')
    project.insertSubject('Ivanov','istec')
    res = project.selectSubjects4Model()
    while res.next():
        print(res.value(1))

