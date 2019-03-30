

Using the Selfie dataset must be limited only to the research purposes

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

selfie_dataset.txt provides the annotations and is structured as <image name> <popularity score> <attributes>

Attributes are as following:

2:partial_faces 3:is_female 4:baby 5:child 6:teenager 7:youth 8:middle_age 9:senior 10:white 11:black 12:asian 13:oval_face 14:round_face 15:heart_face 16:smiling 17:mouth_open 18:frowning 19:wearing_glasses 20:wearing_sunglasses 21:wearing_lipstick 22:tongue_out 23:duck_face 24:black_hair 25:blond_hair 26:brown_hair 27:red_hair 28:curly_hair 29:straight_hair 30:braid_hair 31:showing_cellphone 32:using_earphone 33:using_mirror 34:braces 35:wearing_hat 36:harsh_lighting 37:dim_lighting

p.s. number means the index

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

If you make use of the Selfie dataset please cite the following work:

@inproceedings{kalayeh2015selfie,
  title={How to Take a Good Selfie?},
  author={Kalayeh, Mahdi M and Seifu, Misrak and LaLanne, Wesna and Shah, Mubarak},
  booktitle={Proceedings of the 23rd Annual ACM Conference on Multimedia Conference},
  pages={923--926},
  year={2015},
  organization={ACM}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

How we plan to divide the set:
	is_smiling		 (smiling)
	not_smiling		^(smiling)
	is_ frowning		 (frowning)
	not_frowning		^(frowning)
	good_lighting		^(harsh_lighting V dim_lighting)
	bad_lighting 		 (harsh_lighting V dim_lighting)