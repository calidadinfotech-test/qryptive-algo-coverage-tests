# qryptive-algo-coverage-tests

Static test fixtures for checking how a crypto / PQC code scanner (Qryptive) detects **less common algorithms**.
The code is written to be scanned, not run: libraries are real, but no build or tests are included.

Only the languages Qryptive code scanning supports are used: Python, Java, Go, JavaScript and TypeScript.

| Folder | What it covers |
|---|---|
| `python/public_key.py` | BLS, Schnorr (BIP-340), SM9, GOST R 34.10, ECIES, Paillier, Rabin, JWK `P-256`, EC-KCDSA |
| `python/symmetric.py` | AES-SIV / OCB / GCM-SIV, CAST5, Kuznyechik, Magma, GOST 28147-89, Speck, Simon, PRESENT, Ascon |
| `python/hashes.py` | Keccak-256, SHA-512/256, SHA-512/224, cSHAKE, TupleHash, KangarooTwelve, Streebog, Tiger |
| `python/kdf_mac.py` | KBKDF, ConcatKDF, X9.63 KDF, PBKDF1, bcrypt-pbkdf, yescrypt, md5-crypt, SHA-512-crypt, Balloon, SRP, OPAQUE, SPAKE2 |
| `python/pqc.py` | LMS/HSS, BIKE, Saber, MAYO, UOV, CROSS, SQIsign, HAWK, and broken SIKE, Rainbow, GeMSS, plus Picnic |
| `java/.../PublicKeyAlgos.java` | EC-MQV, EC-GDSA, JCA `SHA256withECDSA`, XML-DSig URI `rsa-sha256` |
| `java/.../BlockCiphers.java` | IDEA, SEED, ARIA, LEA, Kalyna, GOST 28147, Skipjack, TEA, RC5, RC6, Threefish, CBC-MAC, VMAC, UMAC |
| `java/.../Digests.java` | Kupyna, Skein, Tiger, MD6, JH, HAS-160, ParallelHash |
| `java/.../PqcAlgos.java` | NewHope, LMS |
| `go/ciphers.go` | XTEA, AEGIS-128L, Deoxys-II |
| `js/jose_algs.js` | ES256K, JWE A256KW + A256GCM, WebCrypto ECDSA P-256 |
| `js/zk_hashes.js` | Poseidon, MiMC7, Pedersen, Keccak-256 (ethers), Groestl |
| `ts/pq_hybrid.ts` | X-Wing hybrid KEM, Schnorr, BLS12-381 |
| `python/negative_controls.py`, `js/negative_controls.js` | Look-alike words and comments that must **not** be reported |

The expected result for every line is kept in the separate test-case workbook (not in this repo).
