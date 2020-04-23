import cx_Freeze

executables = [cx_Freeze.Executable('lorisClient.py')]

cx_Freeze.setup(name='Loris6',options={'build_exe':{'packages':['pygame'],
                'include_files': ['C2.png','C3.png','C4.png','C5.png','C6.png','C7.png','C8.png','C9.png','C10.png','C11.png','C12.png','C13.png','C14.png',
                                  'D2.png','D3.png','D4.png','D5.png','D6.png','D7.png','D8.png','D9.png','D10.png','D11.png','D12.png','D13.png','D14.png',
                                  'H2.png','H3.png','H4.png','H5.png','H6.png','H7.png','H8.png','H9.png','H10.png','H11.png','H12.png','H13.png','H14.png',
                                  'S2.png','S3.png','S4.png','S5.png','S6.png','S7.png','S8.png','S9.png','S10.png','S11.png','S12.png','S13.png','S14.png',
                                  'joker.png']}},
                executables = executables
                )
