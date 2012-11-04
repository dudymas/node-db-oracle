{
  'conditions': [
    ['OS=="win"', { 
      'variables' : {
        'ORA_HOME%' : 'C:/oraclexe/app/oracle/product/11.2.0/server'#need to make a script to nab this for npm'ers
      }
    } ]
  ],
  "targets": [
    {
      "target_name": "node-db-oracle",
      "sources": [ 'src/*.cc' ],
      'include_dirs': [
        'deps/node-db/deps/pthreads-win32',
        'deps'
      ],
      'dependencies': [
        'deps/node-db/node-db-lib.gyp:node-db'
      ],
      'conditions': [
        ['OS=="win"', {
		      'include_dirs': [
		        '<(ORA_HOME)/oci/include'
		      ],
          'libraries' : [
            '<(ORA_HOME)/oci/lib/MSVC/oci.lib',
            '<(ORA_HOME)/oci/lib/MSVC/ociw32.lib',
            '<(ORA_HOME)/oci/lib/MSVC/kpucb.lib',
            '<(ORA_HOME)/oci/lib/MSVC/oraocci11.lib'
          ]
        }]
      ]
    }
  ]
}