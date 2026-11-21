from database.connection import DatabaseConnection
from hmac import compare_digest
#hmac module is to genrate and verify keyed-hash 
#message authentication codes.....

class AuthQueries:
    @staticmethod
    def insertUserRecord(name,email,phone,password_hash):
        with DatabaseConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO USER(USERNAME,EMAIL,
                    PHONE,HASH_PASSWORD,ROLE,IS_VERIFIED)
                    VALUES(%s,%s,%s,%s,"USER",FALSE)
                    """,(name,email,phone,password_hash),
                )
                user_id = cursor.lastrowid
            connection.commit()
            return user_id
    @staticmethod
    def getUserData(email):
        with DatabaseConnection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """SELECT USERID AS userid,
                    USERNAME as username,EMAIL as email,
                    ROLE as role,
                    IS_ACTIVE as is_active,
                    IS_VERIFIED as is_verified
                    FROM USERS
                    WHERE EMAIL =%s""",(email,),
                )
                return cursor.fetchone()