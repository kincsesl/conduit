"""Username: nem üres
e-mail: Jelszó: 8 betű, egy kis-, egy nagybetű és egy számjegy.
Sikeres regisztráció:
/html/body/div[2]/div/div[2]	Welcome!
/html/body/div[2]/div/div[3]	Your registration was successful!
/html/body/div[2]/div/div[4]/div/button (OK)
"""

# mindenütt érvényes elemek:
cookies_accept = "/html/body/div/footer/div/div/div/div[2]/button[2]/div"  # xpath
cookies_declin = "/html/body/div/footer/div/div/div/div[1]/button[2]/div"
nav_linkek = "nav-link"  # Az elemek class tulajdonsága.
conduitfelirat = "/html/body/div/nav/div/a"  # Link a nyitólapra.

nyitolap = "http://localhost:1667/#/"

signinlap = "http://localhost:1667/#/login"

signuplap = "http://localhost:1667/#/register"
submit = "/html/body/div[1]/div/div/div/div/form/button"
username = "/html/body/div[1]/div/div/div/div/form/fieldset[1]/input"
emil = "/html/body/div[1]/div/div/div/div/form/fieldset[2]/input"
password = "/html/body/div[1]/div/div/div/div/form/fieldset[3]/input"
# Felugró ablak, sikeres:
welcome = "/html/body/div[2]/div/div[2]"  # Welcome! felirat
successful = "/html/body/div[2]/div/div[3]"  # Your registration was successful! felirat
successful_okgomb = "/html/body/div[2]/div/div[4]/div/button"  # (OK) gomb
# Felugró ablak, hibás:
failed = "/html/body/div[2]/div/div[2]"  # Registration failed!
userhiba = ["Username field required.", "Email field required.", "Password field required.",
            "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter."]
reszlet = "/html/body/div[2]/div/div[3]"
failed_okgomb = "/html/body/div[2]/div/div[4]/div/button"
