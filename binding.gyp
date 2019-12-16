{
    "targets": [
        {
            "target_name": "hashing",
            "sources": [
                "hashing.cpp",

                "x16r.c",

                "sha3/sph_blake.h"
                "sha3/sph_bmw.h"
                "sha3/sph_groestl.h"
                "sha3/sph_jh.h"
                "sha3/sph_keccak.h"
                "sha3/sph_skein.h"
                "sha3/sph_luffa.h"
                "sha3/sph_cubehash.h"
                "sha3/sph_shavite.h"
                "sha3/sph_simd.h"
                "sha3/sph_echo.h"
                "sha3/sph_hamsi.h"
                "sha3/sph_fugue.h"
                "sha3/sph_shabal.h"
                "sha3/sph_whirlpool.h"
                "sha3/sph_sha2.h"
            ],
            "include_dirs": [
                "crypto",
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
