# Solution

## TLDR
Weak JSON Web Token (JWT) signing key allows attacker to change data (username) and access other user data (flag)

## Steps

- Once logged in/registered, can see `auth` cookie has JWT data
- This can be confirmed by cyberchef or jwt.io
- To brute force the signing key, you can use hashcat with rockyou.txt
- hashcat jwt.txt -m 16500 -a 3 rockyou.txt
  - jwt.txt holding the JWT
  - `-m 16500` indicates JWT
  - `-a 3` indicates brute force
- This will give you the signing key `starwars`
- You can use this to create your own valid JWT using sites above
- On the main page once logged in, you can see `admin` is logged in, so make your username `admin`
- Enter this new JWT as your auth cookie, refresh, and you should be admin with the flag
