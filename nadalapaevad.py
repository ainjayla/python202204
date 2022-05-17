WEEK_DAYS = ['esmaspaev', 'teisipaev', 'pyhapaev']

i = 0

while i < len(WEEK_DAYS):
    print(WEEK_DAYS[i], \
          'toopaev' if WEEK_DAYS[i] != 'laupaev' and WEEK_DAYS[i] != 'pyhapaev' else 'puhkepaev')
    i += 1