# RSA_Miller-Rabin
A very simple implementation of RSA algorithm using **Miller–Rabin Primality Test** to check if P and Q are prime numbers

## About RSA

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym RSA comes from the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who publicly described the algorithm in 1977. An equivalent system was developed secretly, in 1973 at GCHQ (the British signals intelligence agency), by the English mathematician Clifford Cocks. That system was declassified in 1997.[1]

In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret. Messages can be encrypted by anyone, via the public key, but can only be decoded by someone who knows the prime numbers.[2]

The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the "factoring problem". Breaking RSA encryption is known as the RSA problem. Whether it is as difficult as the factoring problem is an open question.[3] There are no published methods to defeat the system if a large enough key is used.

RSA is a relatively slow algorithm. Because of this, it is not commonly used to directly encrypt user data. More often, RSA is used to transmit shared keys for symmetric key cryptography, which are then used for bulk encryption-decryption.

## About Miller-Rabin Primality Test

The Miller–Rabin primality test or Rabin–Miller primality test is a probabilistic primality test: an algorithm which determines whether a given number is likely to be prime, similar to the Fermat primality test and the Solovay–Strassen primality test.

It is of historical significance for the research of a polynomial-time deterministic primality test. Its probabilistic variant remains widely used in practice, as one of the simplest and fastest tests known.

Gary L. Miller discovered the test in 1976; Miller's version of the test is deterministic, but its correctness relies on the unproven extended Riemann hypothesis.[1] Michael O. Rabin modified it to obtain an unconditional probabilistic algorithm in 1980.[2][a]

