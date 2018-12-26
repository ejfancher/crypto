Objectives/goals
----------------

-   implement a real world example of cryptography

-   improve my cryptographic primitives from previous projects

-   make a well documented addition to my GitHub repository

 

Project Description
-------------------

This project simulates classic ransomware in the form it was when it was first
invented. The inventors called it cryptoviral extortion when they first
presented it in 1996. Quoting from Wikipedia the steps of their cryptoviral
extortion is:

"

1.  [attacker**→**victim] The attacker generates a key pair and places the
    corresponding public key in the malware. The malware is released.

2.  [victim**→**attacker] To carry out the cryptoviral extortion attack, the
    malware generates a random symmetric key and encrypts the victim's data with
    it. It uses the public key in the malware to encrypt the symmetric key. This
    is known as [hybrid
    encryption](https://en.wikipedia.org/wiki/Hybrid_encryption) and it results
    in a small asymmetric ciphertext as well as the symmetric ciphertext of the
    victim's data. It zeroizes the symmetric key and the original plaintext data
    to prevent recovery. It puts up a message to the user that includes the
    asymmetric ciphertext and how to pay the ransom. The victim sends the
    asymmetric ciphertext and e-money to the attacker.

3.  [attacker**→**victim] The attacker receives the payment, deciphers the
    asymmetric ciphertext with the attacker's private key, and sends the
    symmetric key to the victim. The victim deciphers the encrypted data with
    the needed symmetric key thereby completing the cryptovirology attack.

“ (<https://en.wikipedia.org/wiki/Ransomware>)

 

My project follows these guidelines, except since their is no actual attacker or
victim there is no money involved or GUI or other interface to the ransomware.
What I did was write the cryptographic primitives necessary for the attack for
both the attacker and victim’s machine. You can find the attackers primitives in
attacker.py and the victims primitives in ransomware.py.

 

Design
------

Apart from how I divided up the two files for this project, these files are
further divided into classes. In ransomware.py there are classes AES_CTR and
RSA_ENCRYPT. In AES_CTR, I wrote AES in CTR mode for this project as it is a
secure mode of AES. In RSA_ENCRYPT there I wrote the code for encrypting a file
with RSA public key cryptography. In attacker.py there is just the class RSA\_
which implements key generation, encryption and decryption with RSA public key
cryptography.

 

Resources:
----------

-   Python 3

-   PyCryptodome. This library needs to be installed without conflicts including
    those with PyCrypto. Using a python virtualenv is the safest way to get this
    library without conflicts as it will be the only 3rd party library
    installed. See [this
    article](https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv)
    for a great guide on how to get one up and running.

 

References:
-----------

The usage examples of PyCryptodome found at
<https://pycryptodome.readthedocs.io/en/latest/src/examples.html>

<https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html>

 

File Usage:
-----------

python3 attacker.py   —   to generate a RSA key pair

python3 attacker.py \<file\> \<pubKey\> -rsa -e   —   to encrypt a file with RSA

python3 attacker.py \<file\> \<privKey\> \<nonce\> -rsa -d   —   to decrypt a
file with RSA

 

python3 ransomware.py \<file\> -aes -e   —   to encrypt a file with AES in CTR
mode

python3 ransomware.py \<file\> \<key\> -aes -d   —   to decrypt a file with AES
in CTR mode

python3 ransomware.py sym_key \<pubKey\> -rsa -e   —   to encrypt a file with
RSA

 

Example Usage (simulates “cryptoviral extortion” ransomware):
-------------------------------------------------------------

### The hacker generates a RSA key pair on their machine:

(pycryptodome_pipenv) bash-3.2\$ python3 attacker.py 

RSA PRIVATE KEY:

2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d0a4d4949457041494241414b434151454177664e335a345133313136766352776f397475716f7a2f4d6458494d6d554d79624d4d54764e39616d4e4977324759320a6f3661465734702f6530344d7141704d4234672f324c7868394c34323571506c3350727a5a705176476871436e5a6c6e4249675779705874687a35734372476b0a5674457436412b7664626a42585553696e696b456259466a736243654f6b594e526c6477544939684855387a617778723953765a5431503372795572673046680a66663562326945746b425032594a45634368623768544a78676c4246704f7844542f4f655068476e75735169455a634478786e55772f5450576f5a47497353640a716352504232637441646c4d676e72416350712b39525a6c6b79592f47657378554975577848464c5a6266514d554e7355746f6654665759632b57747541654c0a4a33756f4747704f5132454a2f52797869726854466b684e4e36765754356257336576787051494441514142416f4942414165364c707046642b427274756a680a4173484f616f61594372547468476652497155586776426a5a413253305a773235615937574239586f7a4449746f6a675a69586d574167794b493379793947720a4779366b7a4a74473571485a334c5577356a47566e43445a2f494c472f3374366c7a6974526759492b70324d56353834466a3766762f7654362f662b2b494c680a4252343177422f6d466977464c2b41723478755178786276476d6d2b316333593979636c6c6c6a7579576e676555613451632b764a453439676e6b764e6671770a5039774759513347454f67763141515356794748616a72737a2f384c4264646367596f4b6658304d32553939464c596f2f4b2b394b4d5339386d37386c6f594f0a2f312b4175723375676142426139594e4650304c6a4f6f576934786b316a7966543078693379424d6d596b72765637543273466d424d434d422f563369534c510a334236364f6c6b43675945417a5162455975496d41705053394c44526442642f337239514177736a4c397466314e7656776b6631714334486f6d4674566458670a3661386a776837377a565261755330334f54355857716453505055657a7a7656396b5a46525172447667446777374c763245396148436979553074786836792f0a4f3131536b72437545526a656377552b61726a644f68527a314d5847386b57736d734e744d3741474355746c70443679343454426a486b43675945413869764a0a7a624c534b685339556850706671332f2f53636761346a4b323764396b786f3672344a35583738777755486d59517836415839614534385158636856336961510a682f386d59477876564d6f444a5146434a667974472b3853764d6d346d3955496e336b306469776c354a632b4b554c432b2f7145696454415a52702b66714e760a384859656273416152744d5836317950343066694b513734353152434659413244326d7a6134304367594177424a61344a676b4b3733346e7973577a623947460a354c366a6839633833523872706a55424a494e5857546832676d5475426f4a2f6d494a4363366b37704c622b796155325a66426c6a65794831457a62386b4b680a524548793870743367354d676f6d626a2f576d34554a7537514638646a49725a4a336b77572b72596e4439314a7452416748316e6e65536d2f343868724d6e4a0a455634684465664d41336d52707847556b63495732514b4267514476476243377553797267364b516f54784f61506c774e75745a674d765a4e30647972396a310a5a48723176383068596a465637483268634e323870656e677a6d574a5773596b6f4253423630335968304f6e693643463550333973495074686255526c7270570a79644b30516b352f625a7867484a78724d534d652b7347696b524148644e4b5774656a434c4556465844496e6e56497263744f6d2b6a4e6949747a455962762b0a5a37785147514b4267514444557631786658644e6d31674a376f6e437039424f31396d73774272644263464766692f6657792f52792b74344953775a44694b650a4742685474482b6139714a786f515a616b35734f61544d75683374344f5a364f58586f6630694345584f574b694d3944507430336970426a637a3776697053460a78723951472b5049624e7730713454714f5746714c766b476a6738356b783333667369316b366f7a2f6b6559525238683868746949413d3d0a2d2d2d2d2d454e44205253412050524956415445204b45592d2d2d2d2d

RSA PUBLIC KEY:

2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494942496a414e42676b71686b6947397730424151454641414f43415138414d49494243674b434151454177664e335a345133313136766352776f397475710a6f7a2f4d6458494d6d554d79624d4d54764e39616d4e4977324759326f3661465734702f6530344d7141704d4234672f324c7868394c34323571506c3350727a0a5a705176476871436e5a6c6e4249675779705874687a35734372476b5674457436412b7664626a42585553696e696b456259466a736243654f6b594e526c64770a544939684855387a617778723953765a54315033727955726730466866663562326945746b425032594a45634368623768544a78676c4246704f7844542f4f650a5068476e75735169455a634478786e55772f5450576f5a4749735364716352504232637441646c4d676e72416350712b39525a6c6b79592f47657378554975570a7848464c5a6266514d554e7355746f6654665759632b57747541654c4a33756f4747704f5132454a2f52797869726854466b684e4e36765754356257336576780a70514944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d

### The Hacker at this point would copy the private key to file, insert the public key into the ransomware, and deliver the ransomware to the victim. 

### Now on the victims machine:

### here is the user data:

(pycryptodome_pipenv) bash-3.2\$ cat user_data 

more confidential stuff

even more confidential stuff

last line of confidential stuff

### The ransomware encrypts the users data (here “user_data”) with AES in CTR mode. ransomware.py automatically saves the key to file in file called sym_key...

(pycryptodome_pipenv) bash-3.2\$ python3 ransomware.py user_data -aes -e

(pycryptodome_pipenv) bash-3.2\$ cat user_data 

82c36f8b3b6c24eebce75a4eda3e4d50a7de89b5352095e1eba8c7d02fcf1d60654384a18531d98d32efee9435ab878d8c0cc36e9be2eb4eb8d95ed672fea63cb1ce3206c846cc7c8971b9f11742901b68099ec0b3
(pycryptodome_pipenv) bash-3.2\$ 

(pycryptodome_pipenv) bash-3.2\$ cat sym_key 

eadedee1dda019a58aa1d59d5afebd31 5172bd6ad5749180

 

### The ransomware then encrypts the symmetric key with the RSA public key...

(pycryptodome_pipenv) bash-3.2\$ python3 ransomware.py sym_key
2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494942496a414e42676b71686b6947397730424151454641414f43415138414d49494243674b434151454177664e335a345133313136766352776f397475710a6f7a2f4d6458494d6d554d79624d4d54764e39616d4e4977324759326f3661465734702f6530344d7141704d4234672f324c7868394c34323571506c3350727a0a5a705176476871436e5a6c6e4249675779705874687a35734372476b5674457436412b7664626a42585553696e696b456259466a736243654f6b594e526c64770a544939684855387a617778723953765a54315033727955726730466866663562326945746b425032594a45634368623768544a78676c4246704f7844542f4f650a5068476e75735169455a634478786e55772f5450576f5a4749735364716352504232637441646c4d676e72416350712b39525a6c6b79592f47657378554975570a7848464c5a6266514d554e7355746f6654665759632b57747541654c4a33756f4747704f5132454a2f52797869726854466b684e4e36765754356257336576780a70514944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d
-rsa -e

(pycryptodome_pipenv) bash-3.2\$ cat sym_key 

?O\|M?????GnH0?[???d?kŗt?z?v??/??\>??;Pf????w??Fg?:?????'x6?5???6?l??/??v?iB?P??n?.?\$??R6D?PB\@?뺮N?Gw?W?\>t?\\??0\|?
h??1l9??5?4??N?S\<2Ak????H?\<????r?\<???0y???p\@???;??V?a?

                                                                              ?W
??ˣR

   ????(!?Se????O??R\@??ȁ?w ']??\~+?A?[&??\\
???\@-?'??F?KFZ?A?8G?W?jV??????Ar???m{??&A?Ãv??0??d??qLG ?

\~6k?\<C?O??Q????j0?

### On the attackers machine:

### After the attacker receives the encrypted symmetric key and payment the attacker decrypts the symmetric key used to encrypt the users data:

(pycryptodome_pipenv) bash-3.2\$ python3 attacker.py sym_key
2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d0a4d4949457041494241414b434151454177664e335a345133313136766352776f397475716f7a2f4d6458494d6d554d79624d4d54764e39616d4e4977324759320a6f3661465734702f6530344d7141704d4234672f324c7868394c34323571506c3350727a5a705176476871436e5a6c6e4249675779705874687a35734372476b0a5674457436412b7664626a42585553696e696b456259466a736243654f6b594e526c6477544939684855387a617778723953765a5431503372795572673046680a66663562326945746b425032594a45634368623768544a78676c4246704f7844542f4f655068476e75735169455a634478786e55772f5450576f5a47497353640a716352504232637441646c4d676e72416350712b39525a6c6b79592f47657378554975577848464c5a6266514d554e7355746f6654665759632b57747541654c0a4a33756f4747704f5132454a2f52797869726854466b684e4e36765754356257336576787051494441514142416f4942414165364c707046642b427274756a680a4173484f616f61594372547468476652497155586776426a5a413253305a773235615937574239586f7a4449746f6a675a69586d574167794b493379793947720a4779366b7a4a74473571485a334c5577356a47566e43445a2f494c472f3374366c7a6974526759492b70324d56353834466a3766762f7654362f662b2b494c680a4252343177422f6d466977464c2b41723478755178786276476d6d2b316333593979636c6c6c6a7579576e676555613451632b764a453439676e6b764e6671770a5039774759513347454f67763141515356794748616a72737a2f384c4264646367596f4b6658304d32553939464c596f2f4b2b394b4d5339386d37386c6f594f0a2f312b4175723375676142426139594e4650304c6a4f6f576934786b316a7966543078693379424d6d596b72765637543273466d424d434d422f563369534c510a334236364f6c6b43675945417a5162455975496d41705053394c44526442642f337239514177736a4c397466314e7656776b6631714334486f6d4674566458670a3661386a776837377a565261755330334f54355857716453505055657a7a7656396b5a46525172447667446777374c763245396148436979553074786836792f0a4f3131536b72437545526a656377552b61726a644f68527a314d5847386b57736d734e744d3741474355746c70443679343454426a486b43675945413869764a0a7a624c534b685339556850706671332f2f53636761346a4b323764396b786f3672344a35583738777755486d59517836415839614534385158636856336961510a682f386d59477876564d6f444a5146434a667974472b3853764d6d346d3955496e336b306469776c354a632b4b554c432b2f7145696454415a52702b66714e760a384859656273416152744d5836317950343066694b513734353152434659413244326d7a6134304367594177424a61344a676b4b3733346e7973577a623947460a354c366a6839633833523872706a55424a494e5857546832676d5475426f4a2f6d494a4363366b37704c622b796155325a66426c6a65794831457a62386b4b680a524548793870743367354d676f6d626a2f576d34554a7537514638646a49725a4a336b77572b72596e4439314a7452416748316e6e65536d2f343868724d6e4a0a455634684465664d41336d52707847556b63495732514b4267514476476243377553797267364b516f54784f61506c774e75745a674d765a4e30647972396a310a5a48723176383068596a465637483268634e323870656e677a6d574a5773596b6f4253423630335968304f6e693643463550333973495074686255526c7270570a79644b30516b352f625a7867484a78724d534d652b7347696b524148644e4b5774656a434c4556465844496e6e56497263744f6d2b6a4e6949747a455962762b0a5a37785147514b4267514444557631786658644e6d31674a376f6e437039424f31396d73774272644263464766692f6657792f52792b74344953775a44694b650a4742685474482b6139714a786f515a616b35734f61544d75683374344f5a364f58586f6630694345584f574b694d3944507430336970426a637a3776697053460a78723951472b5049624e7730713454714f5746714c766b476a6738356b783333667369316b366f7a2f6b6559525238683868746949413d3d0a2d2d2d2d2d454e44205253412050524956415445204b45592d2d2d2d2d
-d

(pycryptodome_pipenv) bash-3.2\$ cat sym_key 

eadedee1dda019a58aa1d59d5afebd31 5172bd6ad5749180

### At this point the attacker would send the decrypted symmetric key back to the victim, so the victim can recover his/her data.

### The victim decrypts their data:

(pycryptodome_pipenv) bash-3.2\$ python3 ransomware.py user_data \$(cat sym_key)
-aes -d

(pycryptodome_pipenv) bash-3.2\$ cat user_data 

more confidential stuff

even more confidential stuff

last line of confidential stuff