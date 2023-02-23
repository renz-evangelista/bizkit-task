from flask import Blueprint, request
from iteration_utilities import unique_everseen

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    search_list = []

    if "id" in args:
        search_list.extend([user for user in USERS if user['id'] == args['id']])

    if "name" in args:
        search_list.extend([user for user in USERS if args['name'].lower() in user['name'].lower()])

    if "age" in args:
        search_list.extend([user for user in USERS if int(args['age'])-1 <= user['age'] <= int(args['age'])+1])

    if "occupation" in args:
        search_list.extend([user for user in USERS if args['occupation'].lower() in user['occupation'].lower()])
    
    return list(unique_everseen(search_list))
