{
  'targets': [
    {
      'target_name': 'node-db',
      'type' : 'static_library',
      'sources': ['binding.cc', 'events.cc', 'query.cc', 'exception.cc', 'result.cc', 'connection.cc'],
      'conditions': [
        ['OS=="win"', {
          'dependencies': [
            'deps/pthreads-win32/pthread.gyp:pthread'
          ],
          'defines': [
            'strtok_r=strtok_s',
            'PLATFORM=win32'
          ],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'RuntimeLibrary': 0
            },
          }
        }]
      ]
    }
  ]
}