import arcgis
from integration_testing_utils import connect_to_portal

portal_connection = {
                        'portal_url': REMOVED,
                        'admin_username': REMOVED,
                        'admin_password': REMOVED
}

gis = connect_to_portal(  portal_connection['portal_url'], 
                        portal_connection['admin_username'], 
                        portal_connection['admin_password'])

# Test connection to portal
assert gis.url == portal_url, 'Testing the connection to the portal, using an admin account, has failed.'
