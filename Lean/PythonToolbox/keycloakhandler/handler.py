from os import environ as env

from keycloak import KeycloakAdmin


class KeycloakHandler:
    realm_name = 'example_realm'
    realm_user = 'example_user'

    def __init__(self, realm_name, realm_user):
        self.realm_name = realm_name
        self.realm_user = realm_user

        self.keycloak_admin = KeycloakAdmin(
            server_url=f"http://{env.get('KEYCLOAK_HOST')}:{env.get('KEYCLOAK_PORT')}/auth/",
            username=env.get('KEYCLOAK_USER'), password=env.get('KEYCLOAK_PASSWORD'),
            realm_name=self.realm_name, user_realm_name=self.realm_user)

    def get_keycloak_admin(self):
        return self.keycloak_admin

    def get_users(self):
        return self.keycloak_admin.get_users({})

    def get_user_id(self, username):
        return self.keycloak_admin.get_user_id(username)
