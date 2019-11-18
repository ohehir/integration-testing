import arcgis
import os.path
from integration_testing_utils import connect_to_portal
from integration_testing_utils import create_portal_user
from integration_testing_utils import delete_portal_user_and_their_content

portal_connection = {
                        'portal_url': REMOVED,
                        'admin_username': REMOVED,
                        'admin_password': REMOVED
}

creator_user = {
                        'username': REMOVED,
                        'password': REMOVED,
                        'firstname': REMOVED,
                        'lastname': REMOVED,
                        'email': REMOVED,
                        'description': 'test',
                        'role': 'org_publisher',
                        'level': 2,
                        'provider': 'enterprise'
}

gis = connect_to_portal(portal_connection['portal_url'], 
                        portal_connection['admin_username'], 
                        portal_connection['admin_password'])

test_creator = create_portal_user(  gis,
                                    creator_user['username'], 
                                    creator_user['password'], 
                                    creator_user['firstname'], 
                                    creator_user['lastname'], 
                                    creator_user['email'], 
                                    creator_user['description'], 
                                    creator_user['role'], 
                                    creator_user['level'], 
                                    creator_user['provider'])

assert test_creator.username == creator_user['username'], 'Testing adding a user who has a role of creator to the portal has failed.'

delete_portal_user_and_their_content(creator_user['username'])
