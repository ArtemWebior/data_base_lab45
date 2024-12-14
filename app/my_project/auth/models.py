class Branch:
    def __init__(self, branch_id, branch_code, address, city, region, postal_code):
        self.branch_id = branch_id
        self.branch_code = branch_code
        self.address = address
        self.city = city
        self.region = region
        self.postal_code = postal_code

    def to_dict(self):
        return {
            'branch_id': self.branch_id,
            'branch_code': self.branch_code,
            'address': self.address,
            'city': self.city,
            'region': self.region,
            'postal_code': self.postal_code
        }

class User:
    def __init__(self, user_id, full_name, phone_number, email, user_type):
        self.user_id = user_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.user_type = user_type

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'full_name': self.full_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'user_type': self.user_type
        }
    
class Courier:
    def __init__(self, courier_id, full_name, phone_number, branch_id):
        self.courier_id = courier_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.branch_id = branch_id

    def to_dict(self):
        return {
            'courier_id': self.courier_id,
            'full_name': self.full_name,
            'phone_number': self.phone_number,
            'branch_id': self.branch_id
        }

class Operator:
    def __init__(self, operator_id, full_name, phone_number, branch_id):
        self.operator_id = operator_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.branch_id = branch_id

    def to_dict(self):
        return {
            'operator_id': self.operator_id,
            'full_name': self.full_name,
            'phone_number': self.phone_number,
            'branch_id': self.branch_id
        }

class Tariff:
    def __init__(self, tariff_id, weight_limit, price_per_kg, region):
        self.tariff_id = tariff_id
        self.weight_limit = weight_limit
        self.price_per_kg = price_per_kg
        self.region = region

    def to_dict(self):
        return {
            'tariff_id': self.tariff_id,
            'weight_limit': self.weight_limit,
            'price_per_kg': self.price_per_kg,
            'region': self.region
        }
    
class Parcel:
    def __init__(self, parcel_id, tracking_number, sender_id, receiver_id, weight, dimensions, status, creation_date, tariff_id):
        self.parcel_id = parcel_id
        self.tracking_number = tracking_number
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.weight = weight
        self.dimensions = dimensions
        self.status = status
        self.creation_date = creation_date
        self.tariff_id = tariff_id

    def to_dict(self):
        return {
            'parcel_id': self.parcel_id,
            'tracking_number': self.tracking_number,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'weight': self.weight,
            'dimensions': self.dimensions,
            'status': self.status,
            'creation_date': self.creation_date,
            'tariff_id': self.tariff_id
        }
    
class ParcelMovement:
    def __init__(self, movement_id, parcel_id, branch_id, courier_id, movement_date, details):
        self.movement_id = movement_id
        self.parcel_id = parcel_id
        self.branch_id = branch_id
        self.courier_id = courier_id
        self.movement_date = movement_date
        self.details = details

    def to_dict(self):
        return {
            'movement_id': self.movement_id,
            'parcel_id': self.parcel_id,
            'branch_id': self.branch_id,
            'courier_id': self.courier_id,
            'movement_date': self.movement_date,
            'details': self.details
        }

class DeliverySchedule:
    def __init__(self, schedule_id, parcel_id, courier_id, delivery_date):
        self.schedule_id = schedule_id
        self.parcel_id = parcel_id
        self.courier_id = courier_id
        self.delivery_date = delivery_date

    def to_dict(self):
        return {
            'schedule_id': self.schedule_id,
            'parcel_id': self.parcel_id,
            'courier_id': self.courier_id,
            'delivery_date': self.delivery_date
        }

class Feedback:
    def __init__(self, feedback_id, user_id, parcel_id, rating, comment, feedback_date):
        self.feedback_id = feedback_id
        self.user_id = user_id
        self.parcel_id = parcel_id
        self.rating = rating
        self.comment = comment
        self.feedback_date = feedback_date

    def to_dict(self):
        return {
            'feedback_id': self.feedback_id,
            'user_id': self.user_id,
            'parcel_id': self.parcel_id,
            'rating': self.rating,
            'comment': self.comment,
            'feedback_date': self.feedback_date
        }

class Payment:
    def __init__(self, payment_id, parcel_id, amount, payment_date, payment_method):
        self.payment_id = payment_id
        self.parcel_id = parcel_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method

    def to_dict(self):
        return {
            'payment_id': self.payment_id,
            'parcel_id': self.parcel_id,
            'amount': self.amount,
            'payment_date': self.payment_date,
            'payment_method': self.payment_method
        }
