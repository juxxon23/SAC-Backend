from app.helpers.encrypt_pass import Crypt

encrypt = Crypt()


class EdipMiProfile():
    def edit_mi_profile_void(self, sac_user, perfile):
        sac_user.name_u = perfile['name_u']
        sac_user.lastname_u = perfile['lastname_u']
        sac_user.phone_u = perfile['phone_u']
        sac_user.city_u = perfile['city_u']
        sac_user.regional_u = perfile['regional_u']
        sac_user.center_u = perfile['center_u']
        sac_user.email_inst = perfile['email_inst']
        if perfile.get('bonding_type') == "":
            sac_user.bonding_type = 3
        else:
            sac_user.bonding_type = perfile['bonding_type']

    def edit_mi_profile(self, sac_user, perfile):
        sac_user.name_u = perfile['name_u']
        sac_user.lastname_u = perfile['lastname_u']
        sac_user.phone_u = perfile['phone_u']
        sac_user.city_u = perfile['city_u']
        sac_user.regional_u = perfile['regional_u']
        sac_user.center_u = perfile['center_u']
        sac_user.bonding_type = 3


class MyPerfile():
    def my_perfile_void(self, sac_user, perfile):
        sac_user.name_u = perfile['name_u']
        sac_user.lastname_u = perfile['lastname_u']
        sac_user.phone_u = perfile['phone_u']
        sac_user.city_u = perfile['city_u']
        sac_user.regional_u = perfile['regional_u']
        sac_user.center_u = perfile['center_u']
        sac_user.bonding_type = 3

    def my_perfile(self, sac_user, perfile):
        sac_user.password_u = encrypt.hash_string(
            perfile['password_u'])
        sac_user.name_u = perfile['name_u']
        sac_user.lastname_u = perfile['lastname_u']
        sac_user.phone_u = perfile['phone_u']
        sac_user.city_u = perfile['city_u']
        sac_user.regional_u = perfile['regional_u']
        sac_user.center_u = perfile['center_u']
        sac_user.bonding_type = perfile['bonding_type']
