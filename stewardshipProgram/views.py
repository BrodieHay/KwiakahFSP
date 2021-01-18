from django.shortcuts import render

aHealthyForest = [{'image': "https://lh3.googleusercontent.com/fife/ABSRlIrOuquSocohxUlTzQ7uZOhwjXr6XPIbk_frpwQgVDTY-5124DPWnx2UGHvyah21oqwVBnJKB4azSHDey7ZoBpfmXqwjFYWnaJzrCIH8rzFSkOJ3DDIwrKUFQCJ4Rg_Bua3t9_1E-lnNazwvlGa13xGvYjmPEzUOcZTZAQgKvpvVBR-8OLNfkrvpp60N90LvlkMYsTsJ7K25fl66_2nF2PuzPJgAKO-p6t-56wID5zceSQCOrGBHAd2udSn8gDPPzdhOp9SSjnYqpr5DOMEtbG_Xoo10xLGHGAlNpF1TQ0hDlua5HXPOxWLaDibhZmm4jH11aYGtiUwg8aDHHLLx9S2WUgyeSRfXi8Eo95KeOhO4I2YH8NKanfOKUZ7hT2fMiy3GOMe5GdA8xhrNb4lYIJx_p4ur7tqwraL43MtGOGrFf934DZZz0cBpBw5gaLJ0qJc5os6uA50oeV6WxlX8JcwqPKoZkiNEur7LyJVxV5VsuDUoi2TcfrmbGLMbvsdt0Tz-dRrXLyShgS32YYtdMPVKnC7tF_m8oq9enWlhWGDOAHem67PEzBlrzoks-u4wQTMitzDUbESuiD2ymg4ZTShdQLw8BVJHIIp4KsbHBZ1JkuM76Sl4Tp2VkEHV3DCXjlk31TXIJEUPvgWVXXCcA5MhdF5EnEw5SMHzBBZVyahL8ngiHqaxRXGODzEhG3-M-Q9kvil5yVrRuT6dGTt_B8ndhCFEw-E=s1000-w1000-h800-no?authuser=0"},
{'image': "https://lh3.googleusercontent.com/fife/ABSRlIp8Gn7SWBFTiixoZHh4QNRzT0o7Su5rr80RwHre1k7bbjNRow7nvzOv_5C5k2oIaxcCmu6fPUT3sftvfkEbRYsvJ8CTmmCM-bvyMmrrac5-uTztu5x1TrzKKjDYyo82gMIxqYYTzUZg1o-NPcN3zJ9J6_PreBqgMH-rRuprgDSdoE1YDDM18WDRLwXzvDZ5RJHrvAwCS5z7MIdeJtxdOFcP-DQ_LTVwwSVBC0mH1huh_Ov98M84cIkt9vsSkUstQ3t79v_IRXtTTJZdz-SUuOmcTj5YhvCNuGY8x4dQiVd6dSwSsm2rqBLtB-_tU6qFldAbc29nDUTIEJg3HKlsZWX7ys7uNpV8KGE7b-ClL3KREHW3q3kHGQiHFIGdzaGX0BPtaJa9zCbOf6vNExBCp5lAreT3_ihaUGjnM7O4-BBZQQmSVnF9aOKq_Qc8yRVVuVi54TfgcXNXTdL33BGCBwcBLmHf2kIAdUJ-DKoi3gBPI5n3ZVNCt2YNA1AIIX-FlZnaHlam8a_dk8l76wDeW5akVzKh-QOvZ5HMfi1d9-pnjZe544Ec7MsAKn6u3u2e77-cpdClscG0kkOuYL1s67fDciRitG2tqjFSxXQOPyr9jMRA5LAI4bwkfEgbUxutmEYC9srO61iR0zo1MNAaMkZyuCyUkrkMahthlEDaHVYqvxbostgLIgooke8mDmpLH0Dvc59xUFK5thjiGEZoAASGh4XhtLE=s1000-w1000-h800-no?authuser=0"},
{'image': "https://t.ly/V7pQ"}]
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
