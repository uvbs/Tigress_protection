#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_10006 = ref_278 # MOV operation
ref_10584 = ref_10006 # MOV operation
ref_10602 = (ref_10584 >> (0xD & 0x3F)) # SHR operation
ref_10609 = ref_10602 # MOV operation
ref_16394 = ref_278 # MOV operation
ref_17006 = ref_16394 # MOV operation
ref_17024 = ((ref_17006 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17031 = ref_17024 # MOV operation
ref_17685 = ref_10609 # MOV operation
ref_17691 = ref_17031 # MOV operation
ref_17693 = (ref_17691 | ref_17685) # OR operation
ref_18896 = ref_17693 # MOV operation
ref_18904 = ((0x2EA4A1C39AF5800 + ref_18896) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_23895 = ref_18904 # MOV operation
ref_28989 = ref_278 # MOV operation
ref_34051 = ref_23895 # MOV operation
ref_34635 = ref_28989 # MOV operation
ref_34641 = ref_34051 # MOV operation
ref_34643 = ((ref_34635 - ref_34641) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_34651 = ref_34643 # MOV operation
ref_39722 = ref_34651 # MOV operation
ref_45376 = ref_278 # MOV operation
ref_45920 = ref_45376 # MOV operation
ref_45938 = ((ref_45920 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_45945 = ref_45938 # MOV operation
ref_51577 = ref_278 # MOV operation
ref_52205 = ref_51577 # MOV operation
ref_52223 = (ref_52205 >> (0x37 & 0x3F)) # SHR operation
ref_52230 = ref_52223 # MOV operation
ref_52780 = ref_45945 # MOV operation
ref_52786 = ref_52230 # MOV operation
ref_52788 = (ref_52786 | ref_52780) # OR operation
ref_57861 = ref_52788 # MOV operation
ref_63037 = ref_278 # MOV operation
ref_64260 = ref_63037 # MOV operation
ref_64268 = (0x3E908497 | ref_64260) # OR operation
ref_69225 = ref_64268 # MOV operation
ref_76233 = ref_39722 # MOV operation
ref_76885 = ref_76233 # MOV operation
ref_76903 = (ref_76885 >> (0x2 & 0x3F)) # SHR operation
ref_76910 = ref_76903 # MOV operation
ref_77420 = ref_76910 # MOV operation
ref_77436 = (0xF & ref_77420) # AND operation
ref_78726 = ref_77436 # MOV operation
ref_78734 = (0x1 | ref_78726) # OR operation
ref_83892 = ref_23895 # MOV operation
ref_84468 = ref_83892 # MOV operation
ref_84482 = ref_78734 # MOV operation
ref_84484 = (ref_84482 & 0xFFFFFFFF) # MOV operation
ref_84486 = (ref_84468 >> ((ref_84484 & 0xFF) & 0x3F)) # SHR operation
ref_84493 = ref_84486 # MOV operation
ref_91405 = ref_39722 # MOV operation
ref_92033 = ref_91405 # MOV operation
ref_92051 = (ref_92033 >> (0x2 & 0x3F)) # SHR operation
ref_92058 = ref_92051 # MOV operation
ref_92672 = ref_92058 # MOV operation
ref_92688 = (0xF & ref_92672) # AND operation
ref_93899 = ref_92688 # MOV operation
ref_93907 = (0x1 | ref_93899) # OR operation
ref_94572 = ref_93907 # MOV operation
ref_94574 = ((0x40 - ref_94572) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_94582 = ref_94574 # MOV operation
ref_99701 = ref_23895 # MOV operation
ref_100284 = ref_99701 # MOV operation
ref_100298 = ref_94582 # MOV operation
ref_100300 = (ref_100298 & 0xFFFFFFFF) # MOV operation
ref_100302 = ((ref_100284 << ((ref_100300 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_100309 = ref_100302 # MOV operation
ref_100895 = ref_84493 # MOV operation
ref_100901 = ref_100309 # MOV operation
ref_100903 = (ref_100901 | ref_100895) # OR operation
ref_105947 = ref_57861 # MOV operation
ref_111055 = ref_69225 # MOV operation
ref_111649 = ref_105947 # MOV operation
ref_111655 = ref_111055 # MOV operation
ref_111657 = ((ref_111649 - ref_111655) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_111665 = ref_111657 # MOV operation
ref_112401 = ref_100903 # MOV operation
ref_112407 = ref_111665 # MOV operation
ref_112409 = ((ref_112401 - ref_112407) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_112411 = ((((ref_112401 ^ (ref_112407 ^ ref_112409)) ^ ((ref_112401 ^ ref_112409) & (ref_112401 ^ ref_112407))) >> 63) & 0x1) # Carry flag
ref_112417 = ((((ref_112407 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_112411 == 0x1) else 0x0)) # SETB operation
ref_112419 = (ref_112417 & 0xFF) # MOVZX operation
ref_113003 = (ref_112419 & 0xFFFFFFFF) # MOV operation
ref_113005 = ((ref_113003 & 0xFFFFFFFF) & (ref_113003 & 0xFFFFFFFF)) # TEST operation
ref_113010 = (0x1 if (ref_113005 == 0x0) else 0x0) # Zero flag
ref_113012 = (0x1F99 if (ref_113010 == 0x1) else 0x1F6F) # Program Counter


if (ref_113010 == 0x1):
    ref_264469 = SymVar_0
    ref_264484 = ref_264469 # MOV operation
    ref_273944 = ref_264484 # MOV operation
    ref_274556 = ref_273944 # MOV operation
    ref_274574 = (ref_274556 >> (0xD & 0x3F)) # SHR operation
    ref_274581 = ref_274574 # MOV operation
    ref_280127 = ref_264484 # MOV operation
    ref_280777 = ref_280127 # MOV operation
    ref_280795 = ((ref_280777 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_280802 = ref_280795 # MOV operation
    ref_281328 = ref_274581 # MOV operation
    ref_281334 = ref_280802 # MOV operation
    ref_281336 = (ref_281334 | ref_281328) # OR operation
    ref_282634 = ref_281336 # MOV operation
    ref_282642 = ((0x2EA4A1C39AF5800 + ref_282634) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_287850 = ref_282642 # MOV operation
    ref_292734 = ref_264484 # MOV operation
    ref_297756 = ref_287850 # MOV operation
    ref_298402 = ref_292734 # MOV operation
    ref_298408 = ref_297756 # MOV operation
    ref_298410 = ((ref_298402 - ref_298408) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_298418 = ref_298410 # MOV operation
    ref_303495 = ref_298418 # MOV operation
    ref_309127 = ref_264484 # MOV operation
    ref_309755 = ref_309127 # MOV operation
    ref_309773 = ((ref_309755 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_309780 = ref_309773 # MOV operation
    ref_315319 = ref_264484 # MOV operation
    ref_315955 = ref_315319 # MOV operation
    ref_315973 = (ref_315955 >> (0x37 & 0x3F)) # SHR operation
    ref_315980 = ref_315973 # MOV operation
    ref_316644 = ref_309780 # MOV operation
    ref_316650 = ref_315980 # MOV operation
    ref_316652 = (ref_316650 | ref_316644) # OR operation
    ref_321827 = ref_316652 # MOV operation
    ref_326690 = ref_264484 # MOV operation
    ref_327957 = ref_326690 # MOV operation
    ref_327965 = (0x3E908497 | ref_327957) # OR operation
    ref_333097 = ref_327965 # MOV operation
    ref_383732 = ref_321827 # MOV operation
    ref_388762 = ref_333097 # MOV operation
    ref_389398 = ref_383732 # MOV operation
    ref_389404 = ref_388762 # MOV operation
    ref_389406 = (ref_389404 | ref_389398) # OR operation
    ref_390025 = ref_389406 # MOV operation
    ref_390043 = (ref_390025 >> (0x4 & 0x3F)) # SHR operation
    ref_390050 = ref_390043 # MOV operation
    ref_390653 = ref_390050 # MOV operation
    ref_390669 = (0x7 & ref_390653) # AND operation
    ref_391930 = ref_390669 # MOV operation
    ref_391938 = (0x1 | ref_391930) # OR operation
    ref_398249 = ref_303495 # MOV operation
    ref_398901 = ref_398249 # MOV operation
    ref_398919 = (ref_398901 >> (0x4 & 0x3F)) # SHR operation
    ref_398926 = ref_398919 # MOV operation
    ref_399496 = ref_398926 # MOV operation
    ref_399512 = (0xF & ref_399496) # AND operation
    ref_400750 = ref_399512 # MOV operation
    ref_400758 = (0x1 | ref_400750) # OR operation
    ref_405906 = ref_287850 # MOV operation
    ref_406512 = ref_405906 # MOV operation
    ref_406526 = ref_400758 # MOV operation
    ref_406528 = (ref_406526 & 0xFFFFFFFF) # MOV operation
    ref_406530 = ((ref_406512 << ((ref_406528 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_406537 = ref_406530 # MOV operation
    ref_413379 = ref_303495 # MOV operation
    ref_413957 = ref_413379 # MOV operation
    ref_413975 = (ref_413957 >> (0x4 & 0x3F)) # SHR operation
    ref_413982 = ref_413975 # MOV operation
    ref_414644 = ref_413982 # MOV operation
    ref_414660 = (0xF & ref_414644) # AND operation
    ref_415949 = ref_414660 # MOV operation
    ref_415957 = (0x1 | ref_415949) # OR operation
    ref_416638 = ref_415957 # MOV operation
    ref_416640 = ((0x40 - ref_416638) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_416648 = ref_416640 # MOV operation
    ref_421669 = ref_287850 # MOV operation
    ref_422283 = ref_421669 # MOV operation
    ref_422297 = ref_416648 # MOV operation
    ref_422299 = (ref_422297 & 0xFFFFFFFF) # MOV operation
    ref_422301 = (ref_422283 >> ((ref_422299 & 0xFF) & 0x3F)) # SHR operation
    ref_422308 = ref_422301 # MOV operation
    ref_422962 = ref_406537 # MOV operation
    ref_422968 = ref_422308 # MOV operation
    ref_422970 = (ref_422968 | ref_422962) # OR operation
    ref_423579 = ref_422970 # MOV operation
    ref_423593 = ref_391938 # MOV operation
    ref_423595 = (ref_423593 & 0xFFFFFFFF) # MOV operation
    ref_423597 = (ref_423579 >> ((ref_423595 & 0xFF) & 0x3F)) # SHR operation
    ref_423604 = ref_423597 # MOV operation
    ref_428567 = ref_423604 # MOV operation
    ref_429767 = ref_428567 # MOV operation
    ref_429769 = ref_429767 # MOV operation
    endb = ref_429769


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_10006 = ref_278 # MOV operation
    ref_10584 = ref_10006 # MOV operation
    ref_10602 = (ref_10584 >> (0xD & 0x3F)) # SHR operation
    ref_10609 = ref_10602 # MOV operation
    ref_16394 = ref_278 # MOV operation
    ref_17006 = ref_16394 # MOV operation
    ref_17024 = ((ref_17006 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_17031 = ref_17024 # MOV operation
    ref_17685 = ref_10609 # MOV operation
    ref_17691 = ref_17031 # MOV operation
    ref_17693 = (ref_17691 | ref_17685) # OR operation
    ref_18896 = ref_17693 # MOV operation
    ref_18904 = ((0x2EA4A1C39AF5800 + ref_18896) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_23895 = ref_18904 # MOV operation
    ref_28989 = ref_278 # MOV operation
    ref_34051 = ref_23895 # MOV operation
    ref_34635 = ref_28989 # MOV operation
    ref_34641 = ref_34051 # MOV operation
    ref_34643 = ((ref_34635 - ref_34641) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_34651 = ref_34643 # MOV operation
    ref_39722 = ref_34651 # MOV operation
    ref_39724 = ((ref_39722 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_39725 = ((ref_39722 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_39726 = ((ref_39722 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_39727 = ((ref_39722 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_39728 = ((ref_39722 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_39729 = ((ref_39722 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_39730 = ((ref_39722 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_39731 = (ref_39722 & 0xFF) # Byte reference - MOV operation
    ref_45376 = ref_278 # MOV operation
    ref_45920 = ref_45376 # MOV operation
    ref_45938 = ((ref_45920 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_45945 = ref_45938 # MOV operation
    ref_51577 = ref_278 # MOV operation
    ref_52205 = ref_51577 # MOV operation
    ref_52223 = (ref_52205 >> (0x37 & 0x3F)) # SHR operation
    ref_52230 = ref_52223 # MOV operation
    ref_52780 = ref_45945 # MOV operation
    ref_52786 = ref_52230 # MOV operation
    ref_52788 = (ref_52786 | ref_52780) # OR operation
    ref_57861 = ref_52788 # MOV operation
    ref_63037 = ref_278 # MOV operation
    ref_64260 = ref_63037 # MOV operation
    ref_64268 = (0x3E908497 | ref_64260) # OR operation
    ref_69225 = ref_64268 # MOV operation
    ref_121717 = ((((ref_39724) << 8 | ref_39725) << 8 | ref_39726) << 8 | ref_39727) # MOV operation
    ref_122944 = (ref_121717 & 0xFFFFFFFF) # MOV operation
    ref_131851 = ((((ref_39728) << 8 | ref_39729) << 8 | ref_39730) << 8 | ref_39731) # MOV operation
    ref_140588 = (ref_131851 & 0xFFFFFFFF) # MOV operation
    ref_140590 = (((ref_140588 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_140591 = (((ref_140588 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_140592 = (((ref_140588 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_140593 = ((ref_140588 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_141854 = (ref_122944 & 0xFFFFFFFF) # MOV operation
    ref_150646 = (ref_141854 & 0xFFFFFFFF) # MOV operation
    ref_150648 = (((ref_150646 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_150649 = (((ref_150646 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_150650 = (((ref_150646 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_150651 = ((ref_150646 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_155632 = ref_23895 # MOV operation
    ref_162063 = ref_23895 # MOV operation
    ref_162675 = ref_162063 # MOV operation
    ref_162691 = (0x3F & ref_162675) # AND operation
    ref_163310 = ref_162691 # MOV operation
    ref_163328 = ((ref_163310 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_163335 = ref_163328 # MOV operation
    ref_163885 = ref_155632 # MOV operation
    ref_163891 = ref_163335 # MOV operation
    ref_163893 = (ref_163891 | ref_163885) # OR operation
    ref_168949 = ref_163893 # MOV operation
    ref_174013 = ref_69225 # MOV operation
    ref_180325 = ref_168949 # MOV operation
    ref_180945 = ref_180325 # MOV operation
    ref_180961 = (0x1F & ref_180945) # AND operation
    ref_181606 = ref_180961 # MOV operation
    ref_181624 = ((ref_181606 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_181631 = ref_181624 # MOV operation
    ref_182249 = ref_174013 # MOV operation
    ref_182255 = ref_181631 # MOV operation
    ref_182257 = (ref_182255 | ref_182249) # OR operation
    ref_187265 = ref_182257 # MOV operation
    ref_192287 = ref_168949 # MOV operation
    ref_198641 = ref_168949 # MOV operation
    ref_203637 = ref_57861 # MOV operation
    ref_204171 = ref_198641 # MOV operation
    ref_204177 = ref_203637 # MOV operation
    ref_204179 = ((ref_204177 + ref_204171) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_204847 = ref_204179 # MOV operation
    ref_204863 = (0x1F & ref_204847) # AND operation
    ref_205486 = ref_204863 # MOV operation
    ref_205504 = ((ref_205486 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_205511 = ref_205504 # MOV operation
    ref_206133 = ref_192287 # MOV operation
    ref_206139 = ref_205511 # MOV operation
    ref_206141 = (ref_206139 | ref_206133) # OR operation
    ref_211293 = ref_206141 # MOV operation
    ref_218103 = ref_57861 # MOV operation
    ref_223183 = ref_187265 # MOV operation
    ref_223743 = ref_218103 # MOV operation
    ref_223749 = ref_223183 # MOV operation
    ref_223751 = (ref_223749 | ref_223743) # OR operation
    ref_224418 = ref_223751 # MOV operation
    ref_224436 = (ref_224418 >> (0x4 & 0x3F)) # SHR operation
    ref_224443 = ref_224436 # MOV operation
    ref_224979 = ref_224443 # MOV operation
    ref_224995 = (0x7 & ref_224979) # AND operation
    ref_226298 = ref_224995 # MOV operation
    ref_226306 = (0x1 | ref_226298) # OR operation
    ref_232674 = ((((((((ref_140590) << 8 | ref_140591) << 8 | ref_140592) << 8 | ref_140593) << 8 | ref_150648) << 8 | ref_150649) << 8 | ref_150650) << 8 | ref_150651) # MOV operation
    ref_233208 = ref_232674 # MOV operation
    ref_233226 = (ref_233208 >> (0x4 & 0x3F)) # SHR operation
    ref_233233 = ref_233226 # MOV operation
    ref_233847 = ref_233233 # MOV operation
    ref_233863 = (0xF & ref_233847) # AND operation
    ref_235166 = ref_233863 # MOV operation
    ref_235174 = (0x1 | ref_235166) # OR operation
    ref_240191 = ref_211293 # MOV operation
    ref_240823 = ref_240191 # MOV operation
    ref_240837 = ref_235174 # MOV operation
    ref_240839 = (ref_240837 & 0xFFFFFFFF) # MOV operation
    ref_240841 = ((ref_240823 << ((ref_240839 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_240848 = ref_240841 # MOV operation
    ref_247778 = ((((((((ref_140590) << 8 | ref_140591) << 8 | ref_140592) << 8 | ref_140593) << 8 | ref_150648) << 8 | ref_150649) << 8 | ref_150650) << 8 | ref_150651) # MOV operation
    ref_248346 = ref_247778 # MOV operation
    ref_248364 = (ref_248346 >> (0x4 & 0x3F)) # SHR operation
    ref_248371 = ref_248364 # MOV operation
    ref_249033 = ref_248371 # MOV operation
    ref_249049 = (0xF & ref_249033) # AND operation
    ref_250246 = ref_249049 # MOV operation
    ref_250254 = (0x1 | ref_250246) # OR operation
    ref_250919 = ref_250254 # MOV operation
    ref_250921 = ((0x40 - ref_250919) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_250929 = ref_250921 # MOV operation
    ref_256006 = ref_211293 # MOV operation
    ref_256590 = ref_256006 # MOV operation
    ref_256604 = ref_250929 # MOV operation
    ref_256606 = (ref_256604 & 0xFFFFFFFF) # MOV operation
    ref_256608 = (ref_256590 >> ((ref_256606 & 0xFF) & 0x3F)) # SHR operation
    ref_256615 = ref_256608 # MOV operation
    ref_257279 = ref_240848 # MOV operation
    ref_257285 = ref_256615 # MOV operation
    ref_257287 = (ref_257285 | ref_257279) # OR operation
    ref_257830 = ref_257287 # MOV operation
    ref_257844 = ref_226306 # MOV operation
    ref_257846 = (ref_257844 & 0xFFFFFFFF) # MOV operation
    ref_257848 = (ref_257830 >> ((ref_257846 & 0xFF) & 0x3F)) # SHR operation
    ref_257855 = ref_257848 # MOV operation
    ref_262855 = ref_257855 # MOV operation
    ref_264147 = ref_262855 # MOV operation
    ref_264149 = ref_264147 # MOV operation
    endb = ref_264149


print endb & 0xffffffffffffffff