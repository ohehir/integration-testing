import arcgis


def connect_to_portal(portal_url, admin_username, admin_password):
    # Create connection to AGOL portal GIS
    return arcgis.gis.GIS(portal_url, admin_username, admin_password)


def create_portal_user(gis, username, password, firstname, lastname, email, description, role, level, provider):
    return gis.users.create(    username,
                                password,
                                firstname,
                                lastname,
                                email,
                                description,
                                role,
                                level,
                                provider)

def add_data_to_portal(gis, parks_properties, data, owner):
    # Add parks to content and attribute to test_creator
    return gis.content.add(parks_properties, data, thumbnail=None, metadata=None, owner=owner, folder=None)


def publish_data_in_portal(portal_data):
    # Publish data
    return portal_data.publish()

def delete_portal_user_and_their_content(username):
    # Access user account
    user = gis.users.get(username)
    
    # List the items owned by the user
    user_items = user.items()
    
    # Delete items if they exist
    if (len(user_items) > 0):
        for item in user_items:
            item.delete()
    
    # Delete user
    user.delete()
