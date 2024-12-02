MII = 10000
TRA = 1.03

gains = (MII*TRA)

print('Gains Anuel:', gains)

NV_MII = (MII+5000)

NV_TRA = (TRA+0.02)

NV_gains = (NV_MII*NV_TRA)

print('Nouveau Gains:', NV_gains)

MI = (NV_gains-(NV_gains*0.1))

print('Montant Investissement:', MI)

NV_NV_TRA = (NV_TRA-0.01)

Gains_Final = (MI*NV_NV_TRA)

print('Gains Final', Gains_Final)


