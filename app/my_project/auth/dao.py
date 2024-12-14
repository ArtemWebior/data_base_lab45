from .models import *

from flask import current_app


class BranchDAO:
    @staticmethod
    def get_all_branches():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Branch")
            branches = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching branches: {e}")
            branches = []
        finally:
            cursor.close()
        return branches

    @staticmethod
    def get_branch_by_id(branch_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Branch WHERE id = %s", (branch_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching branch: {e}")
            row = None
        finally:
            cursor.close()
        return row

    @staticmethod
    def add_branch(branch_code, address, city, region, postal_code):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO Branch (branch_code, address, city, region, postal_code) VALUES (%s, %s, %s, %s, %s)",
                (branch_code, address, city, region, postal_code)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding branch: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_branch(branch_id, branch_code, address, city, region, postal_code):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                """UPDATE Branch 
                   SET branch_code = %s, address = %s, city = %s, region = %s, postal_code = %s 
                   WHERE id = %s""",
                (branch_code, address, city, region, postal_code, branch_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating branch: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def delete_branch(branch_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM Branch WHERE id = %s", (branch_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting branch: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

class UserDAO:
    @staticmethod
    def get_all_users():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM User")
            users = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching users: {e}")
            users = []
        finally:
            cursor.close()
        return users

    @staticmethod
    def get_user_by_id(user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM User WHERE id = %s", (user_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching user: {e}")
            row = None
        finally:
            cursor.close()
        return row

    @staticmethod
    def add_user(full_name, phone_number, email, user_type):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO User (full_name, phone_number, email, user_type) VALUES (%s, %s, %s, %s)",
                (full_name, phone_number, email, user_type)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_user(user_id, full_name, phone_number, email, user_type):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                """UPDATE User 
                   SET full_name = %s, phone_number = %s, email = %s, user_type = %s 
                   WHERE id = %s""",
                (full_name, phone_number, email, user_type, user_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

# Інші таблиці мають схожу структуру побудови
