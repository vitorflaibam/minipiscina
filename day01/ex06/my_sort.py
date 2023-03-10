def create_dict():
    d = {
        "Hendrix": "1942",
        "Allman": "1946",
        "King": "1925",
        "Clapton": "1945",
        "Johnson": "1911",
        "Berry": "1926",
        "Vaughan": "1954",
        "Cooder": "1947",
        "Page": "1944",
        "Richards": "1943",
        "Hammett": "1962",
        "Cobain": "1967",
        "Garcia": "1942",
        "Beck": "1944",
        "Santana": "1947",
        "Ramone": "1948",
        "White": "1975",
        "Frusciante": "1970",
        "Thompson": "1949",
        "Burton": "1939",
    }

    return d

def my_sort():
    d = create_dict()
    d = sorted(d.items(), key=lambda dic: (dic[1], dic[0]))
    d = dict(d)
    d_keys = d.keys()

    for name in d_keys:
        print(name)


if __name__ == "__main__":
    my_sort()