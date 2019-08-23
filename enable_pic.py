import os
path = os.path.join(os.getcwd(), "src","crypto_sign","ed25519","amd64-51-30k")
target_path = os.path.join(os.getcwd(), "pic_assembly")
os.mkdir(target_path)
tag = "crypto_sign_ed25519_amd64_51_30k_"
fulltags = ['crypto_sign_ed25519_amd64_51_30k_batch_EC2D3', 'crypto_sign_ed25519_amd64_51_30k_batch_MU1', 'crypto_sign_ed25519_amd64_51_30k_batch_2P0', 'crypto_sign_ed25519_amd64_51_30k_batch_ORDER2', 'crypto_sign_ed25519_amd64_51_30k_batch_EC2D4', 'crypto_sign_ed25519_amd64_51_30k_batch_MU0', 'crypto_sign_ed25519_amd64_51_30k_batch_EC2D1', 'crypto_sign_ed25519_amd64_51_30k_batch_MU2', 'crypto_sign_ed25519_amd64_51_30k_batch_4P0', 'crypto_sign_ed25519_amd64_51_30k_batch_ORDER0', 'crypto_sign_ed25519_amd64_51_30k_batch_ORDER3', 'crypto_sign_ed25519_amd64_51_30k_batch_REDMASK51', 'crypto_sign_ed25519_amd64_51_30k_batch_EC2D0', 'crypto_sign_ed25519_amd64_51_30k_batch_2P1234', 'crypto_sign_ed25519_amd64_51_30k_batch_ORDER1', 'crypto_sign_ed25519_amd64_51_30k_batch_MU3', 'crypto_sign_ed25519_amd64_51_30k_batch_4P1234', 'crypto_sign_ed25519_amd64_51_30k_batch_EC2D2', 'crypto_sign_ed25519_amd64_51_30k_batch_MU4']
for filename in os.listdir(path):
    if filename[-2:] == ".s":
        print(filename)
        file = open(os.path.join(path, filename))
        outfile = open(os.path.join(target_path, filename), "w")
        for line in file:
            newline = line
            if tag in line and ":" not in line and "#" not in line and line[0] != '.':
                for fulltag in fulltags:
                    if fulltag in line:
                        newline = line.replace(fulltag, fulltag+'(%rip)')
            outfile.write(newline)
        file.close()
        outfile.close()

