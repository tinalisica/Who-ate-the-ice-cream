# -*- coding: utf-8 -*-.


Eva = {"gender": "TGAAGGACCTTC", "race": "AAAACCTCA", "hair-color": "TTAGCTATCGC", "eye-color": "TTGTGGTGGC", "face-shape": "AGGCCTCA"}

Larisa = {"gender": "TGAAGGACCTTC", "race": "AAAACCTCA", "hair-color": "GCCAGTGCCG", "eye-color": "AAGTAGTGAC", "face-shape": "AGGCCTCA"}

Matej = {"gender": "TGCAGGAACTTC", "race": "AAAACCTCA", "hair-color": "CCAGCAATCGC", "eye-color": "TTGTGGTGGC", "face-shape": "AGGCCTCA"}

Miha = {"gender": "TGCAGGAACTTC", "race": "AAAACCTCA", "hair-color": "GCCAGTGCCG", "eye-color": "GGGAGGTGGC", "face-shape": "GCCACGG"}

suspect = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"


check_Eva = 0
if (Eva["gender"] in suspect and Eva ["race"] in suspect and Eva["hair-color"] in suspect and Eva["eye-color"] in suspect and Eva["face-shape"] in suspect):
    print "The suspect is Eva."
else:
    print "The suspect is not Eva."

check_Larisa = 0
if (Larisa["gender"] in suspect and Larisa ["race"] in suspect and Larisa["hair-color"] in suspect and Larisa["eye-color"] in suspect and Larisa["face-shape"] in suspect):
    print "The suspect is Larisa."
else:
    print "The suspect is not Larisa."

check_Matej = 0
if (Matej["gender"] in suspect and Matej ["race"] in suspect and Matej["hair-color"] in suspect and Matej["eye-color"] in suspect and Matej["face-shape"] in suspect):
    print "The suspect is Matej."
else:
    print "The suspect is not Matej."

check_Miha = 0
if (Miha["gender"] in suspect and Miha["race"] in suspect and Miha["hair-color"] in suspect and Miha["eye-color"] in suspect and Miha["face-shape"] in suspect):
        print "The suspect is Miha."
else:
    print "The suspect is not Miha."







