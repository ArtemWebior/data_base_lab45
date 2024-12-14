from .dao import *

from flask import jsonify, request

class BranchController:
    @staticmethod
    def get_all_branches():
        branches = BranchDAO.get_all_branches()
        return jsonify(branches), 200

    @staticmethod
    def get_branch(branch_id):
        branch = BranchDAO.get_branch_by_id(branch_id)
        if branch:
            return jsonify(branch), 200
        return jsonify({'message': 'Branch not found'}), 404

    @staticmethod
    def add_branch(data):
        if not data or not all(key in data for key in ('branch_code', 'address', 'city', 'region', 'postal_code')):
            return jsonify({'message': 'Invalid data'}), 400
        try:
            BranchDAO.add_branch(
                data['branch_code'],
                data['address'],
                data['city'],
                data['region'],
                data['postal_code']
            )
            return jsonify({'message': 'Branch added successfully!'}), 201
        except Exception as e:
            return jsonify({'message': f'Error adding branch: {e}'}), 500

    @staticmethod
    def update_branch(branch_id, data):
        if not data or not all(key in data for key in ('branch_code', 'address', 'city', 'region', 'postal_code')):
            return jsonify({'message': 'Invalid data'}), 400
        try:
            BranchDAO.update_branch(
                branch_id,
                data['branch_code'],
                data['address'],
                data['city'],
                data['region'],
                data['postal_code']
            )
            return jsonify({'message': 'Branch updated successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error updating branch: {e}'}), 500

    @staticmethod
    def delete_branch(branch_id):
        try:
            BranchDAO.delete_branch(branch_id)
            return jsonify({'message': 'Branch deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting branch: {e}'}), 500

class UserController:
    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        return jsonify(users), 200

    @staticmethod
    def get_user(user_id):
        user = UserDAO.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({'message': 'User not found'}), 404

    @staticmethod
    def add_user(data):
        if not data or not all(key in data for key in ('full_name', 'phone_number', 'email', 'user_type')):
            return jsonify({'message': 'Invalid data'}), 400
        try:
            UserDAO.add_user(
                data['full_name'],
                data['phone_number'],
                data['email'],
                data['user_type']
            )
            return jsonify({'message': 'User added successfully!'}), 201
        except Exception as e:
            return jsonify({'message': f'Error adding user: {e}'}), 500

    @staticmethod
    def update_user(user_id, data):
        if not data or not all(key in data for key in ('full_name', 'phone_number', 'email', 'user_type')):
            return jsonify({'message': 'Invalid data'}), 400
        try:
            UserDAO.update_user(
                user_id,
                data['full_name'],
                data['phone_number'],
                data['email'],
                data['user_type']
            )
            return jsonify({'message': 'User updated successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error updating user: {e}'}), 500

    @staticmethod
    def delete_user(user_id):
        try:
            UserDAO.delete_user(user_id)
            return jsonify({'message': 'User deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting user: {e}'}), 500


class SelectController:
    @staticmethod
    def get_all_stories_with_tags():
        stories = SelectDAO.get_all_stories_with_tags()
        return jsonify(stories), 200

    @staticmethod
    def get_all_users_with_stories():
        stories = SelectDAO.get_all_users_with_stories()
        return jsonify(stories), 200

        
