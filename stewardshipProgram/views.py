from django.shortcuts import render

aHealthyForest = [{'image': "https://lh3.googleusercontent.com/C42Fggzz5zE3YNntJfaLpCt9TljbRsgj5AsP2SKkYtdI0NmJLxYyS3abJPmjcPzAnLT90TL3JxfeEdn6Z8wZU6pJ895xsicAnmQRWvZisu_ZRPNCyNNkKxN7lzhun7IsC2fWKLE5d9Siz8f0uluoBk5Hqv21c00B26aACMpcSsqSlR-Rl1j9CJO22NB19t7NmOITf6VrxLS8E2Rsyb9lpYKuhltgG2G84si16bfzGMBeusZufba-xf8UGggMZkJF6xJck79pfW8bZOOzwiNQ1-pcFJUMoaNwHnldaQtXW2jmTyV2FKtBKAUvSsYhC9qiGHz9VV8NQhDyJvIQNn-3BiJvGDWDlH7tfZCCQSCN6vDD1yNjEqKkJC2Z3yIQ-g6pTz-cSHTkMGQxI_aRuTEiAi8mvMfFF-yiPX7Ep77FIMj7dGm-GdMH6YEAAqfrp4vWcDug0VTH6bLupGRmDZrW-_uwel_xor5pFAZmSqt4mLzgfrE4UVxq8jloR8-cF5odNUtYkGqK9aoyfeymlFLI_ianY_3NZPVM1sVa-Mk3AD7SfSHthFQf7eYuO5vZQJMmk6FiRc_e8gty2VuIDiGrPmh98ZKplDUF_LmjCIKvLPWOX18a4tovpYmMDpZoMbhiUfCs_-ymJHgbITNukNbhoWjli-_JiNxUsTKP_flxCrosp0_mKpSGtTw=w1000-h800-no?authuser=0",
'image': "https://lh3.googleusercontent.com/VPx39HN9curMBQWpT980pQ7aiF0L78oUrcQkhdGdaLPheYFE0ert3VzIJdT6zlqn7cFklfdzW6bvLH3Kfx9h7IS7mK0MXDjb8nfbaM4YlwiS8ePubRKLDCozl5CYqxJSQ-StLG4EEA55R7nI8IGipBxjMJvDvloKrp2IBD3lTGm7WybXG-KFjnP5uvJDGRktUbqXJTk6aV05zqY_5zrOIzaw16obfgAXxEL1_HTVR9lQtpUT8ZTUcWoOxJehZN9rgNRi0qf69ZLX88y1dD_xGp6qw27qu-_vlvp9Tdm7UMfr5syGl67DLovFZUe1qqkIAlq-tjT_R7XlNQw68k59z-1gsePqZ0sJ5n5Cz_Af5mtib4ar1iP52QwuxFvJ_X7lFxFlBQicIcAb9BDgTblL3cQWhKtVdpYyvqK-qnTdzlKTrjS5cV1pVzOsJfatfQwelVClAlA4c6OZCNUeDsm19azY1lIcCcKSiswyJ5ubn0VMZMrrwoWMHTNiBcgKFEgm7ETzGAAwxMTB_KfMHj-1jP-t2Xq7jSEduLkvJxmWgp0YdznocKm302JCwTJbLi07ilK8WMbAlq6oU75H66yEmmXFAXge9oQZL9S51pQubbIpwwGCLDKCTAC3MPspYZpJq-0pjUoJvrrcwR_encFmCWN66Lg3ZG1h218toSSVdmrvfO02gV3ZGdA=w1000-h800-no?authuser=0",
'image': "https://lh3.googleusercontent.com/dm8fUmPOfvaH_0W5sNdzf3FPTYRdk7JyvXLNsLJ50bqz507mpWGyKMTVBZlFw_x_6X1qBEmQrc5MxoVugD6gTnfgGmKO2Pc87CI0RwJqwCtWHJwKKoBgOIzXPA0IljG7IwLmbwEbB0y33xGOxE3kj5u4j9w9mJ22Wn5GxoPEccn0S7NyA4oRrLSBYVjwQ9U_QGz2SXc_ePBb9pPxv-trqClU8vB225dJMgt4Y08P8iBwD64DyTqHU5TeyJebWPUhP7uMTZ6poa-kpNC5l6aQZvoZd1cO5i5vWo1fCS4tl8aHN0DCPeG21LAnXVs7bLY2StuAt9w0K8yeqLYn4498vRJhUlA9VM05nveueJ-vgmrbRf3fYMMZ4d1ufAWkd3JZRQp1Z5sz1NH75g17eV4rd01h7CSXYIllWW7Hx6-dEOgfa27xcJGTndr4y7BMw66s1ME_774YjinVrZm4mv8Dd-YhL0i-LpEcVNjiH1U3vdbVNsFnk5dZf8Lfvs5431vxjL7tPwVtTFJp40sIZD6T-8B0tXqZ32-w-_2d0tJ6TpFdOEYUZaGWFMioK4A4LIZEDa6E0R5_HtmbiBlRyN-1nc3ooJkqlZDeZJdVtAkPpAdJBghnsv42kXqmDwSmslleBaZfx9_rnu8BJg8QHf2F_bUkQl0g-UbTE-flL-oD4P3auUqU5swECVM=w1000-h800-no?authuser=0"}]
dirtAndRoots1 = [{}]
dirtAndRoots2 = [{}]
forestFloor1 = [{}]
forestFloor2 = [{}]
kneeHigh1 = [{}]
kneeHigh2 = [{}]
eyeHigh1 = [{}]
eyeHigh2 = [{}]
skyHigh1 = [{}]
skyHigh2 = [{}]
supportingBiodiversity = [{}]

def home(request):
    return render(request, 'stewardshipProgram/home.html')

def primary(request):
    context = {
        'aHealthyForest' : aHealthyForest
    }
    return render(request, 'stewardshipProgram/primary.html', context)

def preschool(request):
    return render(request, 'stewardshipProgram/preschool.html')

def toddler(request):
    return render(request, 'stewardshipProgram/toddler.html')

def resources(request):
    return render(request, 'stewardshipProgram/resources.html')
