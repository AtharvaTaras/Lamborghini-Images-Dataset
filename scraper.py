from bing_image_downloader import downloader

main = 'lamborghini'
suffixes = ['aventador',
            'aventador sv',
            'aventador svj',
            'aventador j',
            'aventador coupe',
            'aventador roadster',
            'aventador lp',
            'aventador lp ultimae',
            'aventador lp roadster',
            'hurracan sterrato',
            'hurracan tecnia',
            'hurracan sto',
            'hurracan evo',
            'hurracan evo spyder',
            'hurracan evo rwd',
            'hurracan evo rwd spyder',
            'urus s',
            'urus performante',
            'countach lpi 800-4',
            'sian fkp 37',
            'sian roadster',
            'terzo millenio',
            'asterion',
            'estoque',
            'murciélago 6.2',
            'murciélago Roadster',
            'murciélago LP640',
            'murciélago LP640 Roadster',
            'murciélago LP670-4 SV',
            'murciélago R-GT',
            'gallardo 5.0',
            'Gallardo SE',
            'Gallardo Spyder',
            'Gallardo Nera',
            'Gallardo Superleggera',
            'Gallardo LP560-4',
            'Gallardo LP560-4 Spyder',
            'Gallardo LP570-4 Spyder Performante',
            'Gallardo L140']

for car in suffixes:
    name = main + car

    downloader.download(query=name,
                        limit=100,
                        output_dir='data/',
                        adult_filter_off=False)
    