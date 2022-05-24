def kas_raha_jagub(kilo_hind, kogus, olemasolev_raha):
    return True if kilo_hind * kogus <= olemasolev_raha else False

print('Ostan. Raha jagub' if kas_raha_jagub(20, 4.5, 10) else 'Ei osta. Raha on otsas')
