import arcgis
import os.path
from integration_testing_utils import connect_to_portal
from integration_testing_utils import add_data_to_portal
from integration_testing_utils import create_portal_user
from integration_testing_utils import publish_data_in_portal
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
                        'lastname': REMOVED',
                        'email': REMOVED,
                        'description': 'test',
                        'role': 'org_publisher',
                        'level': 2,
                        'provider': 'enterprise'
}

fname = "Parks_and_Open_Space.zip"
    
parks_properties = {
                        'title': 'Parks and Open Space',
                        'tags': 'parks, open data, testing, test, integration tests, sample data',
                        'type': 'Shapefile'
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

# Get data path for sample data
directory = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(directory, fname)

parks_data = add_data_to_portal(gis, parks_properties, data, creator_user['username'])

feature_layer_item = publish_data_in_portal(parks_data)

assert feature_layer_item.created is not None, 'Testing adding data to the portal and publishing it has failed.'

delete_portal_user_and_their_content(creator_user['username'])
