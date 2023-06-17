# Slurm Headers

OKSTATE High-Performance Computing Cluster: Pete
```shell
#!/bin/bash
#SBATCH -J JOB_NAME
#SBATCH -o JOB_NAME.o%j
#SBATCH -p batch
#SBATCH -n 32
#SBATCH -t 5-00:00:00
#SBATCH --mail-type=END
#SBATCH --mail-user=USER_NAME
```

Pittsburgh High-Performance Computing Cluster: BRIDGES2
```shell
#!/bin/bash
#SBATCH -J JOB_NAME
#SBATCH -o JOB_NAME.o%j
#SBATCH -N 1
#SBATCH -p RM-512
#SBATCH -t 4:00:00
#SBATCH --ntasks-per-node=128
#SBATCH --mail-type=END
#SBATCH --mail-user=USER_NAME
```
