# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    'TestReexecution.test_full_pipeline_reexecution_fs_storage[in_memory_instance_in_process_env] 1'
] = {
    'launchPipelineExecution': {
        '__typename': 'LaunchPipelineRunSuccess',
        'run': {
            'mode': 'default',
            'pipeline': {'name': 'csv_hello_world'},
            'runConfigYaml': '<runConfigYaml dummy value>',
            'runId': '<runId dummy value>',
            'status': 'NOT_STARTED',
            'tags': [],
        },
    }
}

snapshots[
    'TestReexecution.test_full_pipeline_reexecution_fs_storage[sqlite_with_sync_run_launcher_in_process_env] 1'
] = {
    'launchPipelineExecution': {
        '__typename': 'LaunchPipelineRunSuccess',
        'run': {
            'mode': 'default',
            'pipeline': {'name': 'csv_hello_world'},
            'runConfigYaml': '<runConfigYaml dummy value>',
            'runId': '<runId dummy value>',
            'status': 'NOT_STARTED',
            'tags': [],
        },
    }
}

snapshots[
    'TestReexecution.test_full_pipeline_reexecution_fs_storage[sqlite_with_default_run_launcher_in_process_env] 1'
] = {
    'launchPipelineExecution': {
        '__typename': 'LaunchPipelineRunSuccess',
        'run': {
            'mode': 'default',
            'pipeline': {'name': 'csv_hello_world'},
            'runConfigYaml': '<runConfigYaml dummy value>',
            'runId': '<runId dummy value>',
            'status': 'NOT_STARTED',
            'tags': [],
        },
    }
}

snapshots[
    'TestReexecution.test_full_pipeline_reexecution_in_memory_storage[in_memory_instance_in_process_env] 1'
] = {
    'launchPipelineExecution': {
        '__typename': 'LaunchPipelineRunSuccess',
        'run': {
            'mode': 'default',
            'pipeline': {'name': 'csv_hello_world'},
            'runConfigYaml': '<runConfigYaml dummy value>',
            'runId': '<runId dummy value>',
            'status': 'NOT_STARTED',
            'tags': [],
        },
    }
}

snapshots[
    'TestReexecution.test_full_pipeline_reexecution_in_memory_storage[sqlite_with_sync_run_launcher_in_process_env] 1'
] = {
    'launchPipelineExecution': {
        '__typename': 'LaunchPipelineRunSuccess',
        'run': {
            'mode': 'default',
            'pipeline': {'name': 'csv_hello_world'},
            'runConfigYaml': '<runConfigYaml dummy value>',
            'runId': '<runId dummy value>',
            'status': 'NOT_STARTED',
            'tags': [],
        },
    }
}

snapshots[
    'TestReexecution.test_full_pipeline_reexecution_in_memory_storage[sqlite_with_default_run_launcher_in_process_env] 1'
] = {
    'launchPipelineExecution': {
        '__typename': 'LaunchPipelineRunSuccess',
        'run': {
            'mode': 'default',
            'pipeline': {'name': 'csv_hello_world'},
            'runConfigYaml': '<runConfigYaml dummy value>',
            'runId': '<runId dummy value>',
            'status': 'NOT_STARTED',
            'tags': [],
        },
    }
}

snapshots[
    'TestReexecution.test_full_pipeline_reexecution_fs_storage[sqlite_with_grpc_run_launcher_in_process_env] 1'
] = {
    'launchPipelineExecution': {
        '__typename': 'LaunchPipelineRunSuccess',
        'run': {
            'mode': 'default',
            'pipeline': {'name': 'csv_hello_world'},
            'runConfigYaml': '<runConfigYaml dummy value>',
            'runId': '<runId dummy value>',
            'status': 'NOT_STARTED',
            'tags': [],
        },
    }
}

snapshots[
    'TestReexecution.test_full_pipeline_reexecution_in_memory_storage[sqlite_with_grpc_run_launcher_in_process_env] 1'
] = {
    'launchPipelineExecution': {
        '__typename': 'LaunchPipelineRunSuccess',
        'run': {
            'mode': 'default',
            'pipeline': {'name': 'csv_hello_world'},
            'runConfigYaml': '<runConfigYaml dummy value>',
            'runId': '<runId dummy value>',
            'status': 'NOT_STARTED',
            'tags': [],
        },
    }
}
