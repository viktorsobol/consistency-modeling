import experiments_data_objects

import modeiling_multiprocessing

read_ips_d = [
    #dc1
    '167.71.48.223',
    # '164.90.170.146', - write ip
    '164.90.162.132',
    '167.71.51.73',
    '167.172.175.190',
    '164.90.160.153',
    '164.90.170.45',
    '164.90.164.236',
    '167.172.163.152',
    '167.172.163.21',

    #dc2
    '178.128.113.62',
    '178.128.113.141',
    '178.128.126.251',
    '178.128.113.154',
    '178.128.113.31',
    '178.128.113.13',
    '178.128.113.158',
    '178.128.113.167',
    '178.128.113.103',
    '178.128.113.110'
]

write_ip_d = '164.90.170.146'

number_of_iterations = 2000

# Stored in one dc1
experiment_1 = experiments_data_objects.ExperimentsInputData(
    experiment_id=1,
    amount_of_instances=20,
    replication_factor=3,
    read_consistency_level='ONE',
    write_consistency_level='ONE',
    write_delay_ms=600,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in one dc2
experiment_2 = experiments_data_objects.ExperimentsInputData(
    experiment_id=2,
    amount_of_instances=20,
    replication_factor=3,
    read_consistency_level='ONE',
    write_consistency_level='ONE',
    write_delay_ms=600,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in on dc
experiment_3 = experiments_data_objects.ExperimentsInputData(
    experiment_id=3,
    amount_of_instances=20,
    replication_factor=3,
    read_consistency_level='ONE',
    write_consistency_level='TWO',
    write_delay_ms=600,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in on dc
experiment_4 = experiments_data_objects.ExperimentsInputData(
    experiment_id=4,
    amount_of_instances=20,
    replication_factor=3,
    read_consistency_level='TWO',
    write_consistency_level='ONE',
    write_delay_ms=600,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in multiple dc, 2 in dc1 and 2 in dc2
experiment_5 = experiments_data_objects.ExperimentsInputData(
    experiment_id=5,
    amount_of_instances=20,
    replication_factor=4,
    read_consistency_level='ONE',
    write_consistency_level='ONE',
    write_delay_ms=900,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in multiple dc, 3 in dc1 and 3 in dc2
experiment_6 = experiments_data_objects.ExperimentsInputData(
    experiment_id=6,
    amount_of_instances=20,
    replication_factor=6,
    read_consistency_level='LOCAL_QUORUM',
    write_consistency_level='LOCAL_QUORUM',
    write_delay_ms=900,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in multiple dc, 3 in dc1 and 3 in dc2
experiment_7 = experiments_data_objects.ExperimentsInputData(
    experiment_id=7,
    amount_of_instances=20,
    replication_factor=6,
    read_consistency_level='ONE',
    write_consistency_level='ONE',
    write_delay_ms=900,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in multiple dc, 3 in dc1 and 3 in dc2
experiment_8 = experiments_data_objects.ExperimentsInputData(
    experiment_id=8,
    amount_of_instances=20,
    replication_factor=6,
    read_consistency_level='TWO',
    write_consistency_level='TWO',
    write_delay_ms=900,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in multiple dc, 3 in dc1 and 3 in dc2
experiment_9 = experiments_data_objects.ExperimentsInputData(
    experiment_id=9,
    amount_of_instances=20,
    replication_factor=6,
    read_consistency_level='ONE',
    write_consistency_level='TWO',
    write_delay_ms=900,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

# Stored in multiple dc, 2 in dc1 and 2 in dc2
experiment_10 = experiments_data_objects.ExperimentsInputData(
    experiment_id=10,
    amount_of_instances=20,
    replication_factor=6,
    read_consistency_level='TWO',
    write_consistency_level='ONE',
    write_delay_ms=900,
    number_of_iterations=number_of_iterations,
    write_ip=write_ip_d,
    read_ips=read_ips_d
)

all_experiments = [
    experiment_1,
    experiment_2,
    experiment_3,
    experiment_4,
    experiment_5,
    experiment_6,
    # experiment_7,
    # experiment_8,
    # experiment_9,
    # experiment_10,
]

def main():
    for experiment in all_experiments:
        modeiling_multiprocessing.main(experiment, 5)


if __name__ == '__main__':
    main()
