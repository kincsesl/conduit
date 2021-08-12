"""Username: nem üres
e-mail: Jelszó: 8 betű, egy kis-, egy nagybetű és egy számjegy.
Sikeres regisztráció:
/html/body/div[2]/div/div[2]	Welcome!
/html/body/div[2]/div/div[3]	Your registration was successful!
/html/body/div[2]/div/div[4]/div/button (OK)
"""

# mindenütt érvényes elemek:
vv = 5
cookies_accept = "/html/body/div/footer/div/div/div/div[2]/button[2]/div"  # xpath
cookies_declin = "/html/body/div/footer/div/div/div/div[1]/button[2]/div"
nav_linkek = "nav-link"  # Az elemek class tulajdonsága.
conduitfelirat = "/html/body/div/nav/div/a"  # Link a nyitólapra.
logout0 = "/html/body/div[1]/nav/div/ul/li[5]/a"  # Link a logoutra (ha van)
logout = "/html/body/div/nav/div/ul/li[5]/a"
nyitolap = "http://localhost:1667/#/"
signinlap = "http://localhost:1667/#/login"
signuplap = "http://localhost:1667/#/register"
navigacios = "//ul[@class = 'nav navbar-nav pull-xs-right']"


# A signuplap.
submit = "/html/body/div[1]/div/div/div/div/form/button"  # A Sign up gomb.
username = "/html/body/div[1]/div/div/div/div/form/fieldset[1]/input"
emil = "/html/body/div[1]/div/div/div/div/form/fieldset[2]/input"
password = "/html/body/div[1]/div/div/div/div/form/fieldset[3]/input"

# Felugró ablak, sikeres:
welcome = "/html/body/div[2]/div/div[2]"  # Welcome! felirat
successful = "/html/body/div[2]/div/div[3]"  # Your registration was successful! felirat
successful_okgomb = "/html/body/div[2]/div/div[4]/div/button"  # (OK) gomb                    "
sikerszoveg = "Your registration was successful!"

# Felugró ablak, hibás:
failed = "/html/body/div[2]/div/div[2]"  # Registration failed!
userhiba = ["Username field required.", "Email field required.", "Password field required.",
            "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter."]
reszlet = "/html/body/div[2]/div/div[3]"
failed_okgomb = "/html/body/div[2]/div/div[4]/div/button"

# A signinlap
signin_emil = "/html/body/div[1]/div/div/div/div/form/fieldset[1]/input"
signin_password = "/html/body/div[1]/div/div/div/div/form/fieldset[2]/input"
signin_gomb = "/html/body/div[1]/div/div/div/div/form/button"

# Nyitólap bejelentkezve
popular_div = "//div[@class = 'sidebar']/div[@class = 'tag-list']"

# Settings a bejelentkezett ürgének
settings_name = "/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[2]/input"
settings_bio = "/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[3]/textarea"
settings_emil = "/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[4]/input"
settings_password = "/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[5]/input"
settings_submit = "/html/body/div[1]/div/div/div/div/form/fieldset/button"
settings_updatesuccessfull = "/html/body/div[2]/div/div[3]/div/button"

# A New Article oldal
article_url = "http://localhost:1667/#/editor"
article_title = "/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[1]/input"
article_about = "/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[2]/input"
article_write = "/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[3]/textarea"
article_tags = "/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input"
article_publishgomb = "/html/body/div[1]/div/div/div/div/form/button"
article_comment = "/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[1]/textarea"
article_postgomb = "/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[2]/button"
