Last login: Mon May 12 13:35:49 on ttys001
(base) ruchitasolanki@MacBook-Air ~ % ssh ruchita.solanki@arc.ucalgary.ca
ruchita.solanki@arc.ucalgary.ca's password: 
===========================================================================
                    __________________________
                        __     ____       __
                        / |    /    )   /    )
                    ---/__|---/___ /---/------
                      /   |  /    |   /
                    _/____|_/_____|__(____/___
                                    arc                                    

Please note:
 - WE DO NOT PERFORM BACKUPS
 - /scratch usage: If you want to use the larger quota in /scratch, use
         /scratch/$SLURM_JOB_ID as the scratch directory for your job.
 - /scratch/$SLURM_JOB_ID directories will be automatically deleted 
         5 days after the job finishes.

               Problems or deficiencies? Send email to:
                       support@hpc.ucalgary.ca

===========================================================================

SYSTEM NOTICES:
************************************************************************
2025/04/28
--- Interactive Job Timelimit Is Now Enforced

In order to improve the scheduling and job throughput efficiency of ARC, 
interactive jobs are now limited to a maximum of 5 hours of runtime.  
Interactive jobs that are submitted with a timelimit over 5 hours will be 
rejected at submission time.
Apr 29, 2025
To increase the security posture of the Arc cluster administrators will be 
installing Trend Micro on cluster login nodes over the week starting Apr 30.  
Please report any inconsistencies to support@hpc.ucalgary.ca

===========================================================================
Last login: Mon May 12 13:55:16 2025 from 10.12.61.138
Your account quotas as of Mon May 12 22:12:50 MDT 2025:
Filesystem           Used / Total            Files Used / Total
----------       -------- / ----------       ---------- / ----------
Home Directory     83.5GB / 500.0GB (16%)       1.1 Mil / 1.5 Mil (77%)
/scratch            0.0TB / 15.0TB (0%)           0.0 K / 1000.0 K (0%)
/tmp (on arc)       0.0GB / 100.0GB (0%)          0.0 K / Unlimited
/work/ebg_lab      78.5TB / 100.0TB (79%)       0.0 Bil / 2.0 Bil (1%)

You may check your quota using the 'arc.quota' command.

(base) [ruchita.solanki@arc ~]$ z RS
(base) [ruchita.solanki@arc RS]$ cd metatranscriptomics/
(base) [ruchita.solanki@arc metatranscriptomics]$ ls
DL1  GE22  GE7  PL4
(base) [ruchita.solanki@arc metatranscriptomics]$ cd PL4
(base) [ruchita.solanki@arc PL4]$ ls
RS-PL4-1-RNA_S15_L001_R1_001.fastq.gz  RS-PL4-3-RNA_S17_R1_merged.fastq.gz
RS-PL4-1-RNA_S15_L001_R2_001.fastq.gz  RS-PL4-3-RNA_S17_R2_merged.fastq.gz
RS-PL4-1-RNA_S15_L002_R1_001.fastq.gz  sealrpkm_RS-PL4-1-RNA_S15_R1.txt
RS-PL4-1-RNA_S15_L002_R2_001.fastq.gz  sealrpkm_RS-PL4-1-RNA_S15_R2.txt
RS-PL4-1-RNA_S15_R1_merged.fastq.gz    sealrpkm_RS-PL4-2-RNA_S16_R1.txt
RS-PL4-1-RNA_S15_R2_merged.fastq.gz    sealrpkm_RS-PL4-2-RNA_S16_R2.txt
RS-PL4-2-RNA_S16_L001_R1_001.fastq.gz  sealrpkm_RS-PL4-3-RNA_S17_R1.txt
RS-PL4-2-RNA_S16_L001_R2_001.fastq.gz  sealrpkm_RS-PL4-3-RNA_S17_R2.txt
RS-PL4-2-RNA_S16_L002_R1_001.fastq.gz  seal.sbatch
RS-PL4-2-RNA_S16_L002_R2_001.fastq.gz  sealstats_RS-PL4-1-RNA_S15_R1.txt
RS-PL4-2-RNA_S16_R1_merged.fastq.gz    sealstats_RS-PL4-1-RNA_S15_R2.txt
RS-PL4-2-RNA_S16_R2_merged.fastq.gz    sealstats_RS-PL4-2-RNA_S16_R1.txt
RS-PL4-3-RNA_S17_L001_R1_001.fastq.gz  sealstats_RS-PL4-2-RNA_S16_R2.txt
RS-PL4-3-RNA_S17_L001_R2_001.fastq.gz  sealstats_RS-PL4-3-RNA_S17_R1.txt
RS-PL4-3-RNA_S17_L002_R1_001.fastq.gz  sealstats_RS-PL4-3-RNA_S17_R2.txt
RS-PL4-3-RNA_S17_L002_R2_001.fastq.gz  slurm-34970905.out
(base) [ruchita.solanki@arc PL4]$ less slurm-34970905.out
(base) [ruchita.solanki@arc PL4]$ ls
RS-PL4-1-RNA_S15_L001_R1_001.fastq.gz  RS-PL4-2-RNA_S16_R2_merged.fastq.gz    sealrpkm_RS-PL4-3-RNA_S17_R1.txt
RS-PL4-1-RNA_S15_L001_R2_001.fastq.gz  RS-PL4-3-RNA_S17_L001_R1_001.fastq.gz  sealrpkm_RS-PL4-3-RNA_S17_R2.txt
RS-PL4-1-RNA_S15_L002_R1_001.fastq.gz  RS-PL4-3-RNA_S17_L001_R2_001.fastq.gz  seal.sbatch
RS-PL4-1-RNA_S15_L002_R2_001.fastq.gz  RS-PL4-3-RNA_S17_L002_R1_001.fastq.gz  sealstats_RS-PL4-1-RNA_S15_R1.txt
RS-PL4-1-RNA_S15_R1_merged.fastq.gz    RS-PL4-3-RNA_S17_L002_R2_001.fastq.gz  sealstats_RS-PL4-1-RNA_S15_R2.txt
RS-PL4-1-RNA_S15_R2_merged.fastq.gz    RS-PL4-3-RNA_S17_R1_merged.fastq.gz    sealstats_RS-PL4-2-RNA_S16_R1.txt
RS-PL4-2-RNA_S16_L001_R1_001.fastq.gz  RS-PL4-3-RNA_S17_R2_merged.fastq.gz    sealstats_RS-PL4-2-RNA_S16_R2.txt
RS-PL4-2-RNA_S16_L001_R2_001.fastq.gz  sealrpkm_RS-PL4-1-RNA_S15_R1.txt       sealstats_RS-PL4-3-RNA_S17_R1.txt
RS-PL4-2-RNA_S16_L002_R1_001.fastq.gz  sealrpkm_RS-PL4-1-RNA_S15_R2.txt       sealstats_RS-PL4-3-RNA_S17_R2.txt
RS-PL4-2-RNA_S16_L002_R2_001.fastq.gz  sealrpkm_RS-PL4-2-RNA_S16_R1.txt       slurm-34970905.out
RS-PL4-2-RNA_S16_R1_merged.fastq.gz    sealrpkm_RS-PL4-2-RNA_S16_R2.txt
(base) [ruchita.solanki@arc PL4]$ history
    8  conda create -y --name anvio-8 python=3.10
    9  ls
   10  exit
   11  z RS
   12  ls
   13  cd sodalinema/
   14  ls
   15  cd faa
   16  ls
   17  cd ..
   18  zip faa faa.zip
   19  zip faa.zip faa
   20  ls
   21  rm faa.zip 
   22  zip faa.zip faa/*
   23  pwd
   24  exit
   25  z RS
   26  cd metatranscriptomics/
   27  ls
   28  cd DL1/
   29  ls
   30  less slurm-34691408.out
   31  less RS-DL1-1-RNA_S12_R1_paired.fastq.gz
   32  less trim.txt
   33  less merged_trimmed
   34  cd merged_trimmed/
   35  ls
   36  cd ..
   37  ls
   38  rm -r merged_trimmed 
   39  ls
   40  ll RS-DL1-2-RNA_S13_R1_paired.fastq.gz
   41  ll RS-DL1-2-RNA_S13_R1_unpaired.fastq.gz
   42  ll RS-DL1-2-RNA_S13_R1.fastq.gz  
   43  rm *unpaired.fastq.gz
   44  ls
   45  cp trim.txt ../
   46  cd ../
   47  ls
   48  nano trim.txt
   49  exit
   50  z RS
   51  ls
   52  cd sodalinema/
   53  ls
   54  zip fna.zip fna/*
   55  ls
   56  cd fna/
   57  ls
   58  cd ..
   59  zip fna.zip fna/*.fna 
   60  ls
   61  exit
   62  z RS
   63  ls
   64  cd sodalinema/
   65  ls
   66  cd fna/
   67  ls
   68  z RS
   69  ls
   70  cd mags_of_interest/
   71  ls
   72  cd ..
   73  cd pan_genomics/
   74  ls
   75  cd sodali/
   76  ls
   77  cd ..
   78  ls
   79  cd ..
   80  ls
   81  less sodalinema
   82  cd sodalinema/
   83  ls
   84  less tree_of_mags.py
   85  cd fna/
   86  ls
   87  cd ..
   88  cd faa/
   89  ls
   90  cd ..
   91  ls
   92  cd metaerg_out/
   93  ls
   94  cd comparative_genomics/
   95  ls
   96  exit
   97  z RS
   98  cd sodalinema/
   99  ls
  100  cd faa
  101  ls
  102  nano orthologues.py
  103  nano ortho.sh
  104  sbatch ortho.sh
  105  squeue -u ruchita.solanki
  106  ls
  107  cat slurm-34874049.out
  108  ls
  109  wget https://github.com/kinestetika/ComparativeGenomics.git
  110  ls
  111  mkdir script
  112  rm ComparativeGenomics.git 
  113  mv orthologues.py script/
  114  mv ortho.sh script/
  115  rm slurm-34874049.out 
  116  ls
  117  cd script/
  118  wget https://github.com/kinestetika/ComparativeGenomics/archive/refs/heads/master.zip
  119  ls
  120  unzip master.zip master/
  121  unzip master/ master.zip 
  122  unzip ./ master.zip 
  123  unzip master.zip 
  124  ls
  125  rm master.zip 
  126  cd ComparativeGenomics-master/
  127  ls
  128  cd src/
  129  ls
  130  cd comparative_genomics/
  131  ls
  132  pwd
  133  cd ../../../
  134  ls
  135  nano ortho.sh 
  136  sbatch ortho.sh
  137  ls
  138  less slurm-34874098.out 
  139  cd ComparativeGenomics-master/
  140  ls
  141  less README.md 
  142  python3 setup.py 
  143  makepgk
  144  makepkg
  145  python3 setup.py install
  146  ls
  147  cd build/
  148  ls
  149  cd lib/
  150  ls
  151  cd comparative_genomics/
  152  ls
  153  pwd
  154  cd ../../../
  155  ls
  156  cd ..
  157  ls
  158  nano ortho.sh 
  159  sbatch ortho.sh
  160  less slurm-34874103.out 
  161  nano ortho.sh 
  162  sbatch ortho.sh
  163  ls
  164  rm slurm-34874098.out 
  165  rm slurm-34874103.out 
  166  less slurm-34874117.out 
  167  ls
  168  cd ..
  169  cat script/ortho.sh
  170  mkdir orth_output
  171  cd script/
  172  ls
  173  rm slurm-34874117.out 
  174  sbatch ortho.sh
  175  ls
  176  less slurm-34874119.out 
  177  nano ortho.sh
  178  rm slurm-34874119.out 
  179  sbatch ortho.sh
  180  ls
  181  less slurm-34874132.out 
  182  cp ortho.sh tree.sh
  183  nano tree.sh 
  184  sbatch tree.sh
  185  ls
  186  rm slurm-34874132.out 
  187  watch less slurm-34874193.out 
  188  less slurm-34874193.out 
  189  ls
  190  z RS
  191  ls
  192  cd sodalinema/
  193  ls
  194  cd faa  
  195  ls
  196  scancel 34874193
  197  mv GE22_mb12.faa ../
  198  mv GE22_mb9.faa ../
  199  cd script/
  200  less slurm-34874193.out 
  201  rm slurm-34874193.out 
  202  sbatch tree.sh
  203  ls
  204  less slurm-34874223.out
  205  cd ..
  206  ls
  207  cd script/
  208      git clone https://github.com/soedinglab/MMseqs.git
  209  pwd
  210  export MMDIR=/work/ebg_lab/gm/RS/sodalinema/faa/script
  211  ls
  212  export MMDIR=/work/ebg_lab/gm/RS/sodalinema/faa/script/MMseqs
  213  export PATH=$PATH:$MMDIR/bin
  214  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MMDIR/lib/ffindex/src
  215      cd $MMDIR/lib/ffindex
  216      make
  217      cd $MMDIR/src
  218  make
  219  mmseqs
  220  cd ..
  221  ls
  222  cd bin/
  223  ls
  224  cd ../src/
  225  ls
  226  make
  227  ls
  228  cd ..
  229  ls
  230  rm -r MMseqs/
  231  ls
  232  rm slurm-34874223.out 
  233  ls
  234  rm ortho.sh!
  235  rm ortho.sh~
  236  ls
  237  rm -r hmm
  238  rm -r hmm_clusters/
  239  ls
  240  rm -r alignments/
  241  rm -r clustering/
  242  ls
  243  exit
  244  watch squeue -u ruchita.solanki
  245  exit
  246  module avail
  247  exit
  248  z RS
  249  cd sodalinema/
  250  ls
  251  pwd
  252  ls
  253  rm aa.zip 
  254  rm faa.zip 
  255  rm fna.zip 
  256  ls
  257  cd align_output/
  258  ls
  259  cd ../
  260  ls
  261  less align.sh 
  262  mv GC* fna/
  263  ls
  264  conda env list
  265  conda activate gtdbtk-2.4.0
  266  nano align.sh
  267  sbatch align.sh
  268  watch squeue -u ruchita.solanki
  269  ls
  270  less slurm-34892127.out
  271  nano align.sh 
  272  sbatch align.sh
  273  watch squeue -u ruchita.solanki
  274  ls
  275  cd align2_output 
  276  ls
  277  cd align/
  278  ls
  279  pwd
  280  ls
  281  cd ../..
  282  ls
  283  cd fna/
  284  ls
  285  cd ..
  286  cd align2_output/
  287  ls
  288  cd align/
  289  ls
  290  less gtdbtk.bac120.msa.fasta.gz
  291  exit
  292  z RS
  293  ls
  294  cd pan_genomics/
  295  ls
  296  rm -r alkalimonas
  297  ls
  298  rm prokka.sbatch 
  299  rm slurm-34491682.out 
  300  ls
  301  cd ..
  302  ls
  303  cd sodalinema/
  304  ls
  305  rm slurm*
  306  ls
  307  rm tree_of_mags.py 
  308  ;s
  309  ls
  310  cd faa/
  311  ;s
  312  ls
  313  cd ../fna/
  314  ls
  315  mv GCA_049974805.1_ASM4997480v1_genomic.fna GCA_049974805.fna
  316  mv GCF_000332355.1_ASM33235v1_genomic.fna GCF_000332355.fna
  317  ls
  318  z
  319  cd /work/ebg_lab/eb/
  320  ;s
  321  ls
  322  cd diatom_consortia/
  323  ls
  324  cd ..
  325  ls 
  326  cd Shotgun_metagenomics_2024/
  327  ls
  328  cd Data/
  329  ls
  330  exit
  331  z RS
  332  ls
  333  cd sodalinema/
  334  ls
  335  mv GCA_007693465.1_ASM769346v1_genomiccopy2.fna GCA_007693465_2.fna
  336  mv GCA_007693465.1_ASM769346v1_genomiccopy3.fna GCA_007693465_3.fna 
  337  mv GCA_007693465.1_ASM769346v1_genomiccopy.fna GCA_007693465.fna 
  338  ls
  339  rm GC*
  340  ls
  341  mv GCA_007126595.1_ASM712659v1_genomic.fna GCA_007126595.fna
  342  mv GCA_007693465.1_ASM769346v1_genomic.fna GCA_007693465.fna
  343  mv GCA_011390555.1_ASM1139055v1_genomic.fna GCA_011390555.fna
  344  mv GCA_020832215.1_ASM2083221v1_genomic.fna GCA_020832215.fna 
  345  mv GCF_900149785.1_Phormidium_lacuna_genomic.fna GCF_900149785.fna
  346  ls
  347  mv *.fna fna/
  348  ls
  349  cd fna/
  350  ls
  351  conda env list
  352  conda activate gtdbtk-2.4.0 
  353  ls
  354  nano classify.sh
  355  sbatch classify.sh
  356  ls
  357  less slurm-34897203.out
  358  rm -r gtdbtk_classify_wf
  359  mv classify.sh ../
  360  cd ../
  361  ls
  362  nano classify.sh 
  363  cd fna/
  364  ls
  365  mkdir fna
  366  ls
  367  mv fna/ fna_subs
  368  ls
  369  mv ani.sbatch fna_subs/
  370  mv QUERY_LIST fna_subs/ 
  371  mv REFERENCE_LIST 
  372  mv REFERENCE_LIST fna_subs/
  373  mv sodalinema_output fna_subs/
  374  rm slurm-34*
  375  ls
  376  mv fna_subs ../
  377  cd ../
  378  sbatch classify.sh
  379  ls
  380  cd fna
  381  ls
  382  cd ../
  383  ;s
  384  ls
  385  less slurm-34897253.out
  386  nano classify.sh 
  387  sbatch classify.sh
  388  nano checkm2.sh
  389  sbatch checkm2.sh
  390  scancel 34897475
  391  conda activatw
  392  conda activate checkm2
  393  sbatch checkm2.sh
  394  ls
  395  less slurm-34897285.out
  396  tail slurm-34897285.out
  397  ls
  398  cd classify_wf 
  399  ls
  400  pwd
  401  cd ..
  402  ;s
  403  ls
  404  cd CheckM2/
  405  ls
  406  pwd
  407  cd ..
  408  ls
  409  cd fna
  410  ls
  411  cd ../
  412  ls
  413  cd fna_
  414  cd fna_subs/
  415  ls
  416  mv * ../fna
  417  ls
  418  cd ../
  419  rm -r fna
  420  ls
  421  rm -r fna_subs 
  422  ls
  423  rm slurm*
  424  ls
  425  clear
  426  mkdir fna
  427  ls
  428  unzip upload.zip
  429  ls
  430  rm -r upload.zip
  431  rm -r fna  
  432  less upload
  433  z GE22
  434  conda deactivate
  435  z GE22
  436  ls
  437  cd Refinement_GE22/maxbin2_bins/
  438  ls
  439  cp bin.2.fa /work/ebg_lab/gm/RS/sodalinema/upload/
  440  cp bin.3.fa /work/ebg_lab/gm/RS/sodalinema/upload/
  441  cp bin.6.fa /work/ebg_lab/gm/RS/sodalinema/upload/
  442  cp bin.9.fa /work/ebg_lab/gm/RS/sodalinema/upload/
  443  cp bin.12.fa /work/ebg_lab/gm/RS/sodalinema/upload/
  444  cd /work/ebg_lab/gm/RS/sodalinema/upload/
  445  ls
  446  cd ..
  447  ls
  448  cd faa/
  449  ls
  450  cd ../metaerg_out/
  451  ls
  452  cd fna/
  453  ls
  454  mv GE22_mb12.fna /work/ebg_lab/gm/RS/sodalinema/upload/
  455  mv GE22_mb2.fna /work/ebg_lab/gm/RS/sodalinema/upload/
  456  mv GE22_mb*.fna /work/ebg_lab/gm/RS/sodalinema/upload/
  457  mv GE7_bin11.fna /work/ebg_lab/gm/RS/sodalinema/upload/
  458  mv PL4_bin13.fna /work/ebg_lab/gm/RS/sodalinema/upload/
  459  mv DL1_bin26.fna /work/ebg_lab/gm/RS/sodalinema/upload/
  460  cd ../../
  461  cd upload/
  462  ls
  463  rm *.fa
  464  ls
  465  mv GCA_001314905.1_ASM131490v1_genomic.fna "
  466  mv GCA_001314905.1_ASM131490v1_genomic.fna Phormidium_sp_OSCR.fna
  467  mv GCA_001637315.1_ASM163731v1_genomic.fna Phormidium willei_BDU_130791.fna
  468  mv GCA_001637315.1_ASM163731v1_genomic.fna Phormidium_willei_BDU_130791.fna
  469  ls
  470  mv GCA_001657325.1_ASM165732v1_genomic.fna Geitlerinema_sp_BBD_1991_9.fna
  471  mv GCA_003566575.1_ASM356657v1_genomic.fna Cyanobacteria_T3Sed10_304.fna
  472  ls
  473  mv GCA_004299065.1_ASM429906v1_genomic.fna Phormidium_sp_SL48-SHIP.fna
  474  ls
  475  mv GCA_007126595.1_ASM712659v1_genomic.fna Phormidium_sp_CSSed162.fna
  476  mv GCA_007131565.1_ASM713156v1_genomic.fna  Phormidium_spCSSed.fna
  477  ls
  478  mv GCA_007693465.1_ASM769346v1_genomic.fna Phormidium sp_GEM2_Bin31.fna
  479  mv GCA_007693465.1_ASM769346v1_genomic.fna Phormidium_sp_GEM2_Bin31.fna
  480  ls
  481  mv GCA_011390555.1_ASM1139055v1_genomic.fna Phormidium_sp_S10_Bin050.fna
  482  mv GCA_017746765.1_ASM1774676v1_genomic.fna Cyanobacteria_SBC.fna
  483  ls
  484  mv GCA_020386575.1_ASM2038657v1_genomic.fna Ca_S_alkaliphilum.fna
  485  mv GCA_020832215.1_ASM2083221v1_genomic.fna Phormidium_sp_Bin_17.fna
  486  mv GCA_023983615.1_ASM2398361v1_genomic.fna "
  487  mv GCA_023983615.1_ASM2398361v1_genomic.fna Phormidium_yuhuli_AB48.fna
  488  ls
  489  mv GCA_049974805.1_ASM4997480v1_genomic.fna Baaleninema_sp.fna
  490  mv GCA_900149785.2_Phormidium_lacuna_genomic.fna Phormidium_lacuna.fna
  491  ls
  492  mv GCF_000332355.1_ASM33235v1_genomic.fna Baaleninema_simplex_PCC_7105.fna
  493  mv GCF_009846485.1_ASM984648v1_genomic.fna Sodalinema_B-353.fna
  494  ls
  495  mv GCF_012911965.1_ASM1291196v1_genomic.fna Geitlerinema_sp_P-1104.fna
  496  ls
  497  cd ..
  498  ls
  499  rm __MACOSX  
  500  rm -r __MACOSX  
  501  ls
  502  exit
  503  z RS
  504  ls
  505  cd Cyano-three-peaks-pacBio/
  506  ls
  507  cd GE7
  508  ls
  509  less gtdb.sbatch  
  510  watch squeue -u ruchita.solanki
  511  less gtdb.sbatch  
  512  watch squeue -u ruchita.solanki
  513  less checkm2.txt 
  514  watch squeue -u ruchita.solanki
  515  cd /work/ebg_lab/eb/diatom_consortia/
  516  ls
  517  cd MAGS_dorado/
  518  ls
  519  ll
  520  ll -al
  521  ls -l
  522  cd flye_out/
  523  ls
  524  cd busco-e
  525  ls
  526  cd run_eukaryota_odb10/
  527  ls
  528  cd ../../
  529  ls
  530  cd lineages
  531  ls
  532  cd eukaryota_odb10/
  533  ls
  534  cd ../
  535  cd ..
  536  l
  537  ls
  538  cd ../
  539  ls
  540  cd trash/
  541  ls
  542  z RS
  543  ls
  544  cd sodalinema/
  545  ls
  546  cd upload/
  547  ls
  548  less Baaleninema_sp.fna  
  549  ls
  550  mv GCF_046483825.1_ASM4648382v1_genomic.fna sodalinema_sp.fna
  551  ;s
  552  ls
  553  cd ../
  554  ls
  555  nano fa_erg.sbatch
  556  sbatch fa_erg.sbatch
  557  watch squeue -u ruchita.solanki
  558  ls
  559  nano fa_erg.sbatch
  560  cd upload/
  561  ls
  562  cd ../
  563  ls
  564  mkdir trash
  565  mv faa/ trash/
  566  mv gtdbtk_classify_wf  trash/
  567  mv classify_wf/ trash/
  568  ls
  569  mv identify_output/ trash/
  570  mv identify2_output/ trash/
  571  mv align*_output trash/
  572  ls
  573  less  slurm-34901730.out
  574  watch squeue -u ruchita.solanki
  575  ls
  576  cd upload/
  577  ls
  578  watch squeue -u ruchita.solanki
  579  cd ../
  580  less slurm-34901730.out 
  581  ls
  582  cd upload/
  583  ls
  584  watch squeue -u ruchita.solanki
  585  exit
  586  z RS
  587  cd sodalinema/
  588  ls
  589  cd upload/
  590  ls
  591  squeue -u ruchita.solanki
  592  cd faa
  593  ls
  594  cd ../
  595  ls
  596  nano align.sh 
  597  conda env list
  598  conda activate gtdbtk-2.4.0
  599  ls
  600  sbatch align.sh
  601  watch squeue -u ruchita.solanki
  602  ls
  603  less slurm-34910602.out 
  604  nano align.sh 
  605  rm -r identify3_output
  606  ls
  607  sbatch align.sh
  608  watch squeue -u ruchita.solanki
  609  less 34910620
  610  less slurm-34910620
  611  less slurm-34910620.out 
  612  less align.sh 
  613  gtdbtk identify -h
  614  nano align.sh 
  615  ls
  616  rm -r identify3_output/
  617  ls
  618  cd upload/
  619  ls
  620  cd fna/
  621  ls
  622  cd ..
  623  ls
  624  cd ..
  625  ls
  626  sbatch align.sh
  627  watch squeue -u ruchita.solanki
  628  ls
  629  watch squeue -u ruchita.solanki
  630  ls
  631  cd identify3_output/
  632  ls
  633  cd identify/
  634  ls
  635  cd ..
  636  cd ../
  637  nano align.sh 
  638  sbatch align.sh
  639  watch squeue -u ruchita.solanki
  640  ls
  641  cd align3_output/
  642  ls
  643  cd align/
  644  ls
  645  pwd
  646  unzip gtdbtk.bac120.user_msa.fasta.gz
  647  gunzip gtdbtk.bac120.user_msa.fasta.gz
  648  ls
  649  cd ..
  650  ;s
  651  ls
  652  cd ..
  653  ls
  654  mv metaerg_out/ trash/
  655  ls
  656  cd upload/
  657  ;s
  658  ls
  659  exit
  660  z RS
  661  cd sodalinema/
  662  ls
  663  nano classify.sh 
  664  cd upload/
  665  ls
  666  cd ..
  667  conda env list
  668  conda activate gtdbtk-2.4.0
  669  sbatch classify.sh
  670  watch squeue -u ruchita.solanki
  671  ls
  672  less slurm-34932886.out
  673  tail slurm-34932886.out
  674  ls
  675  cd bgs_classify_wf/
  676  ls
  677  less gtdbtk.bac120.summary.tsv
  678  pwd
  679  cd ../
  680  ls
  681  cd ..
  682  ls
  683  cd metatranscriptomics/
  684  ls
  685  cd GE7
  686  ls
  687  ll
  688  cd ..
  689  ls
  690  cd ..
  691  ls
  692  cd metatranscriptomics/
  693  rm trim.txt 
  694  cd so
  695  cd ../sodalinema/
  696  ls
  697  mv slurm* trash/
  698  ls
  699  cd ..
  700  ls
  701  chmod 777 metatranscriptomics/
  702  ls
  703  chmod 777 sodalinema/
  704  ls
  705  pwd
  706  cd sodalinema/
  707  ls
  708  chmod 777 ./
  709  ls
  710  chmod 777 -R ./
  711  ls
  712  chmod 777 -R ./
  713  ls
  714  chmod 777 -R upload/
  715  ls
  716  cd upload/
  717  ls
  718  cd gbk/
  719  ls
  720  pwd
  721  cd ..
  722  ls
  723  cd fna
  724  ls
  725  exit
  726  z RS
  727  cd DL1
  728  z DL1
  729  ls
  730  cd Refinement_pypolca_DL1/metawrap_50_10_bins/
  731  ls
  732  pwd
  733  z RS
  734  cd sodalinema/
  735  ls
  736  cd upload
  737  ls
  738  cd gbk/
  739  ls
  740  z PL4
  741  ls
  742  cd Refinement_pypolca_PL4/metawrap_50_10_bins/
  743  ls
  744  cd ..
  745  ls
  746  less metawrap_50_10_bins.stats
  747  z GE7
  748  ls
  749  cd Refinement_pypolca_GE7/
  750  ls
  751  less metawrap_50_10_bins.stats 
  752  z RS
  753  cd sodalinema/
  754  ls
  755  cd upload/
  756  cd fna/
  757  ls
  758  cd ../
  759  zip fna/
  760  zip fna/*.fna
  761  zip fna.zip fna/
  762  ls
  763  cd fna.zip
  764  pwd
  765  rm -r fna.zip 
  766  ls
  767  zip -r fna.zip fna/
  768  exit
  769  z RS
  770  cd metatranscriptomics/PL4
  771  ls
  772  watch squeu -u ruchita.solanki
  773  watch squeue -u ruchita.solanki
  774  z PL4
  775  ls
  776  cd Refinement_pypolca_PL4/metawrap_50_10_bins/
  777  ls
  778  pwf
  779  pwd
  780  watch squeue -u ruchita.solanki
  781  ls
  782  cd ..
  783  ls
  784  cd ..
  785  ls
  786  cd metaerg  
  787  ls
  788  less bin13.annotations.sqlite
  789  less bin13.fa
  790  nano sqlite.py
  791  python3 sqlite.py 
  792  ls
  793  nano sqlite.py
  794  ls
  795  less bin13.fna
  796  nano sqlite.py 
  797  rm sqlite.py 
  798  nano sqlite_to_fasta.py
  799  python3 sqlite_to_fasta.py 
  800  ls
  801  module avail
  802  z
  803  conda install biopython sqlite
  804  z ERROR: Could not find a version that satisfies the requirement metaerg (from versions: none)
  805  ls
  806  exit
  807  close
  808  exit
  809  pip install metaerg first
  810  pip install metaerg
  811  ls
  812  arc.quota
  813  conda install pysqlite3
  814  conda install biopython
  815  exit
  816  module avail
  817  conda create -n bowtie2
  818  conda activate bowtie2
  819  conda install bioconda::bowtie2
  820  module load miniconda3/bowtie2  
  821  bowtie2 --help
  822  module unload
  823  conda deactivate
  824  module load bbmap/38.84 
  825  seal.sh -h
  826  z RS
  827  cd metatranscriptomics/
  828  ls
  829  cd DL1 
  830  ls
  831  ll
  832  rm *paired*
  833  ls
  834  rm RS-DL1-1-RNA_S12_R1.fastq.gz
  835  rm RS-DL1-1-RNA_S12_R2.fastq.gz  
  836  rm RS-DL1-2-RNA_S13_R1.fastq.gz  
  837  rm RS-DL1-2-RNA_S13_R2.fastq.gz 
  838  rm RS-DL1-3-RNA_S14_R1.fastq.gz
  839  rm RS-DL1-3-RNA_S14_R2.fastq.gz
  840  ls
  841  rm slurm
  842  rm slurm*
  843  rm trim.txt 
  844  ls
  845  cd ../
  846  ls
  847  cd GE22
  848  ls
  849  cd ../GE7
  850  ls
  851  cd ../PL4
  852  s
  853  ls
  854  nano seal.sbatch
  855  ls
  856  nano seal.sbatch 
  857  sbatch seal.sbatch
  858  less seal.sbatch 
  859  scancel  34965315
  860  ls
  861  z PL4
  862  ls
  863  cd me
  864  cd metaerg/
  865  ls
  866  cd html/
  867  ls
  868  cd ../temp/
  869  ls
  870  cd ..
  871  ls
  872  pip install metaerg
  873  rm sqlite_to_fasta.py
  874  nano sqlite.py
  875  python3 sqlite.py 
  876  ls
  877  rm sqlite.py
  878  nano sqlite_to_fasta.py
  879  python3 sqlite_to_fasta.py 
  880  exit
  881  z PL4
  882  cd metaerg/
  883  ls
  884  python3 sqlite_to_fasta.py 
  885  conda activate test_env 
  886  python3 sqlite_to_fasta.py 
  887  ls
  888  mkdir sqlit
  889  cp bin13.annotations.sqlite 
  890  cp bin13.annotations.sqlite sqlit
  891  mv sqlite_to_fasta.py sqlit
  892  cd sqlit/
  893  ls
  894  mv sqlite_to_fasta.py ../
  895  ls
  896  cd ../
  897  ls
  898  python3 sqlite_to_fasta.py
  899  ls
  900  cd sqlit
  901  ls
  902  cd ..
  903  ;s
  904  ls
  905  rm sqlit
  906  rm -r sqlit
  907  rm sqlite_to_fasta.py
  908  ls
  909  from pathlib import Path
  910  from metaerg.datatypes import sqlite
  911  import os
  912  # the working_dir is /work/ebg_lab/eb/overwinter/2025Apr/soda_lake_mags
  913  working_dir = Path(os.getcwd())
  914  annotations_dir = working_dir / "annotations.sqlite"
  915  for sqlite_file in annotations_dir.glob("G*"):
  916      print(f"\nProcessing file: {sqlite_file.name}")
  917      fa_filename = sqlite_file.with_suffix('.fa')
  918      print(f"Creating FASTA file: {fa_filename.name}")
  919      try:
  920          db_connection = sqlite.connect_to_db(sqlite_file)
  921          with open(fa_filename, 'w') as fa_file:
  922              for feature in sqlite.read_all_features(db_connection):
  923                  fa_file.write(f">{feature.id} ({feature.descr}) ({feature.taxon})\n")
  924                  fa_file.write(f"{feature.nt_seq}\n\n")
  925          print(f"Successfully wrote {fa_filename.name}")
  926      except Exception as e:
  927          print(f"Error processing {sqlite_file.name}: {str(e)}")
  928      finally:
  929          if 'db_connection' in locals():
  930              db_connection.close()         del db_connection
  931  print("\nProcessing complete.")
  932  python3
  933  nano sqlite.py
  934  python3 sqlite.py 
  935  ls
  936  nano sqlite.py 
  937  python3 sqlite.py 
  938  ls
  939  nano sqlite.py 
  940  python3 sqlite.py 
  941  ls
  942  nano sqlite.py 
  943  python3 sqlite.py 
  944  ls /work/ebg_lab/gm/RS/Cyano-three-peaks-pacBio/PL4/metaerg/bin13.annotations.sqlite
  945  nano sqlite.py 
  946  python3 sqlite.py 
  947  ls
  948  less bin13.annotations.fa 
  949  cd ../../
  950  cd ../
  951  ls
  952  cd metatranscriptomics/
  953  cd PL4
  954  ls
  955  nano seal.sbatch
  956  sbatch seal.sbatch
  957  conda deactivate
  958  module list
  959  module avail
  960  module load bbmap/38.84 
  961  module load ebg_java/11.0.1
  962  module load bbmap/38.84 
  963  scancel 34970889
  964  sbatch seal.sbatch
  965  ls
  966  top
  967  ls
  968  less seal.sbatch 
  969  ls
  970  less slurm-34970905.out
  971  ls
  972  less slurm-34970905.out
  973  ls
  974  less slurm-34970905.out
  975  less sealrpkm_RS-PL4-1-RNA_S15_R2.txt
  976  ls
  977  less slurm-34970905.out
  978  exit
  979  conda create -n test_env python=3.11 sqlite biopython
  980  z RS
  981  cd PL4
  982  z PL4
  983  cd metaerg/
  984  ls
  985  pwd
  986  ls
  987  z
  988  conda activate test_env
  989  pip install metaerg
  990  python3 
  991  conda deactivate
  992  z RS
  993  z PL4
  994  ls
  995  cd metaerg/
  996  ls
  997  pwd
  998  watch squeue -u ruchita.solanki
  999  exit
 1000  z RS
 1001  cd metatranscriptomics/
 1002  ls
 1003  cd PL4
 1004  ls
 1005  less slurm-34970905.out
 1006  ls
 1007  history
(base) [ruchita.solanki@arc PL4]$ z PL4
(base) [ruchita.solanki@arc PL4]$ ls
bam2depth.sbatch                        medaka.polypolish.polca.PL4.assembly.fasta  run_assembly.sbatch
Binning_pypolca_PL4                     metaerg                                     run_bam2fastq.sbatch
CheckM2                                 metaerg.sbatch                              run_basecalling.sbatch
checkm2.txt                             metaMDBG_PL4                                run_longreadQC.sbatch
CoverM_LR_outputs                       minimap2.sbatch                             run_medaka.sbatch
CoverM_SR_outputs                       PL4_coverm-LR.sbatch                        run_metawrap.sbatch
Filtered_500_10_PL4_LongReads.fastq.gz  PL4_coverm-SR.sbatch                        run_polypolish.sbatch
gtdb.sbatch                             PL4.sorted.bam                              run_pypolca.sbatch
gtdbtk_classify_wf                      Refinement_pypolca_PL4                      sam2bam.sbatch
(base) [ruchita.solanki@arc PL4]$ cd metaerg/
(base) [ruchita.solanki@arc metaerg]$ ls
bin13.annotations.fa       bin13.fa   bin13.gbk                 genome_properties.xls  sqlite.py
bin13.annotations.feather  bin13.faa  bin13.rna.fna             html                   temp
bin13.annotations.sqlite   bin13.fna  genome_properties.sqlite  log.txt
(base) [ruchita.solanki@arc metaerg]$ less sqlite.py
(base) [ruchita.solanki@arc metaerg]$ cd ../../../
(base) [ruchita.solanki@arc RS]$ cd metatranscriptomics/PL4
(base) [ruchita.solanki@arc PL4]$ ls
RS-PL4-1-RNA_S15_L001_R1_001.fastq.gz  RS-PL4-2-RNA_S16_R2_merged.fastq.gz    sealrpkm_RS-PL4-3-RNA_S17_R1.txt
RS-PL4-1-RNA_S15_L001_R2_001.fastq.gz  RS-PL4-3-RNA_S17_L001_R1_001.fastq.gz  sealrpkm_RS-PL4-3-RNA_S17_R2.txt
RS-PL4-1-RNA_S15_L002_R1_001.fastq.gz  RS-PL4-3-RNA_S17_L001_R2_001.fastq.gz  seal.sbatch
RS-PL4-1-RNA_S15_L002_R2_001.fastq.gz  RS-PL4-3-RNA_S17_L002_R1_001.fastq.gz  sealstats_RS-PL4-1-RNA_S15_R1.txt
RS-PL4-1-RNA_S15_R1_merged.fastq.gz    RS-PL4-3-RNA_S17_L002_R2_001.fastq.gz  sealstats_RS-PL4-1-RNA_S15_R2.txt
RS-PL4-1-RNA_S15_R2_merged.fastq.gz    RS-PL4-3-RNA_S17_R1_merged.fastq.gz    sealstats_RS-PL4-2-RNA_S16_R1.txt
RS-PL4-2-RNA_S16_L001_R1_001.fastq.gz  RS-PL4-3-RNA_S17_R2_merged.fastq.gz    sealstats_RS-PL4-2-RNA_S16_R2.txt
RS-PL4-2-RNA_S16_L001_R2_001.fastq.gz  sealrpkm_RS-PL4-1-RNA_S15_R1.txt       sealstats_RS-PL4-3-RNA_S17_R1.txt
RS-PL4-2-RNA_S16_L002_R1_001.fastq.gz  sealrpkm_RS-PL4-1-RNA_S15_R2.txt       sealstats_RS-PL4-3-RNA_S17_R2.txt
RS-PL4-2-RNA_S16_L002_R2_001.fastq.gz  sealrpkm_RS-PL4-2-RNA_S16_R1.txt       slurm-34970905.out
RS-PL4-2-RNA_S16_R1_merged.fastq.gz    sealrpkm_RS-PL4-2-RNA_S16_R2.txt
(base) [ruchita.solanki@arc PL4]$ ls .txt
ls: cannot access '.txt': No such file or directory
(base) [ruchita.solanki@arc PL4]$ ls *.txt
sealrpkm_RS-PL4-1-RNA_S15_R1.txt  sealrpkm_RS-PL4-3-RNA_S17_R1.txt   sealstats_RS-PL4-2-RNA_S16_R1.txt
sealrpkm_RS-PL4-1-RNA_S15_R2.txt  sealrpkm_RS-PL4-3-RNA_S17_R2.txt   sealstats_RS-PL4-2-RNA_S16_R2.txt
sealrpkm_RS-PL4-2-RNA_S16_R1.txt  sealstats_RS-PL4-1-RNA_S15_R1.txt  sealstats_RS-PL4-3-RNA_S17_R1.txt
sealrpkm_RS-PL4-2-RNA_S16_R2.txt  sealstats_RS-PL4-1-RNA_S15_R2.txt  sealstats_RS-PL4-3-RNA_S17_R2.txt
(base) [ruchita.solanki@arc PL4]$ nano tpm_calculator.py
(base) [ruchita.solanki@arc PL4]$ python3 tpm_calculator.py 
Traceback (most recent call last):
  File "/work/ebg_lab/gm/RS/metatranscriptomics/PL4/tpm_calculator.py", line 2, in <module>
    import pandas as pd
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/__init__.py", line 49, in <module>
    from pandas.core.api import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/api.py", line 47, in <module>
    from pandas.core.groupby import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/groupby/__init__.py", line 1, in <module>
    from pandas.core.groupby.generic import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/groupby/generic.py", line 68, in <module>
    from pandas.core.frame import DataFrame
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/frame.py", line 149, in <module>
    from pandas.core.generic import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/generic.py", line 193, in <module>
    from pandas.core.window import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/window/__init__.py", line 1, in <module>
    from pandas.core.window.ewm import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/window/ewm.py", line 11, in <module>
    import pandas._libs.window.aggregations as window_aggregations
ImportError: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/_libs/window/aggregations.cpython-311-x86_64-linux-gnu.so)
(base) [ruchita.solanki@arc PL4]$ nano tpm_calculator_v1.py
(base) [ruchita.solanki@arc PL4]$ python3 tpm_calculator_v1.py 
Traceback (most recent call last):
  File "/work/ebg_lab/gm/RS/metatranscriptomics/PL4/tpm_calculator_v1.py", line 2, in <module>
    import pandas as pd
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/__init__.py", line 49, in <module>
    from pandas.core.api import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/api.py", line 47, in <module>
    from pandas.core.groupby import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/groupby/__init__.py", line 1, in <module>
    from pandas.core.groupby.generic import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/groupby/generic.py", line 68, in <module>
    from pandas.core.frame import DataFrame
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/frame.py", line 149, in <module>
    from pandas.core.generic import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/generic.py", line 193, in <module>
    from pandas.core.window import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/window/__init__.py", line 1, in <module>
    from pandas.core.window.ewm import (
  File "/home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/core/window/ewm.py", line 11, in <module>
    import pandas._libs.window.aggregations as window_aggregations
ImportError: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /home/ruchita.solanki/miniconda3/lib/python3.11/site-packages/pandas/_libs/window/aggregations.cpython-311-x86_64-linux-gnu.so)
(base) [ruchita.solanki@arc PL4]$ module avail
--------------------------------------------------------------------------------- /global/software/Modules/5.5.0/modulefiles ----------------------------------------------------------------------------------
abaqus/2017                  Gaussian16/b01-nehalem        lib/gtest/2020-02-28                                            nvhpc/nvhpc-nompi_21.7    uofl/amber/18_cuda                                    
abaqus/2019                  Gaussian16/b01-skylake        lib/hdf5/1.10.0.1                                               nvhpc/nvhpc_21.7          uofl/amber/18_cuda8                                   
abaqus/2022                  gcc/5.3.0                     lib/hdf5/1.10.0.1-mpi                                           nwchem/6.8.47             uofl/amber/18p17_at19p9_gnu485_openmpi312gnu          
abaqus/2023                  gcc/6.1.0                     lib/hdf5/1.10.5-gnu730_openmpi402gnu730                         ollama/0.3.10             uofl/amber/18p17_at19p9_gnu485_openmpi312gnu_cuda8    
afni/1.4.4                   gcc/7.3.0                     lib/hdf5/1.10.5-gnu730_openmpi402opagnu730                      ollama/0.5.4              uofl/amber/18p17_at19p9_intel20193_openmpi312gnu_mkl  
amber/tools-23               gcc/9.4.0                     lib/hdf5/1.14.5                                                 ollama/0.5.12             uofl/g16/b01                                          
ansys/2019r2                 gcc/10.2.0                    lib/hdf5/1.14.5-mpi                                             openbabel/2.4.1           use.own                                               
ansys/2020r2                 gcc/13.3.0                    lib/hwloc/2.4.1                                                 openmpi/3.0.1-dschulz     utils/arc                                             
ansys/2021r1                 gerris/20131206               lib/itk/4.8.2                                                   openmpi/3.1.2-gnu         valgrind/3.15.0                                       
ansys/2024r1                 gerris/20131206p1             lib/itk/5.2.0                                                   openmpi/3.1.2-intel       vasp/5.4.4-ss                                         
ants/2.3.1                   git/2.25.0                    lib/libgd/2.3.3                                                 openmpi/3.1.2-opa         vmd/1.9.3                                             
ants/2.5.0                   globus-cli/3.3.0              lib/libgit2/1.5.1                                               openmpi/3.1.2-opa2        vscode-server/4.11.0                                  
ants/20191017                gnu-parallel/20181122         lib/libpng/1.6.39                                               openmpi/4.0.2-gnu730      vscode-server/4.96.4                                  
bart/0.8.00                  gnuplot/5.4.6                 lib/libxc/6.2.2                                                 openmpi/4.0.2-opa_gnu730  
bazel/5.2.0                  go/1.13                       lib/mimic/2.0.2                                                 openmpi/4.1.1-gnu         
bcl2fastq2/v2.20             grace/5.1.25                  lib/mpfr/4.1.0                                                  orca/5.0.4-shared         
beast/1.10.4                 gromacs/2016.3-gnu            lib/netcdf/4.9.2                                                orca/5.0.4-static         
beast/2.6.3                  gromacs/2018.0-gnu            lib/netcdf/c-4.7.3_f-4.5.2_gnu730_hdf51105_openmpi402gnu730     osgeo/gdal/3.0.2          
bindcraft/1.5.0              gromacs/2019.6-legacy         lib/netcdf/c-4.7.3_f-4.5.2_gnu730_hdf51105_openmpi402opagnu730  osgeo/geos/3.8.0          
biobuilds/2017.11            gromacs/2019.6-skylake        lib/netcdf/c_4.4.1_f_4.4.4                                      osgeo/proj/6.2.1          
biobuilds/conda              gromacs/2020.6                lib/netcdf/c_4.4.1_f_4.4.4_gnu_serial                           paraview/5.13.1           
bioconda/2024-10             gromacs/2022.6                lib/netcdf/c_4.4.1_f_4.4.4_intel                                perl/5.32.0               
cellranger/arc-2.0.2         gromacs/2023.4                lib/netpbm/10.73                                                perl/5.38.2               
cellranger/atac-v1.2.0       gromacs/2024.3                lib/nifticlib/3.0.2                                             perl_modules/5.16.3       
cellranger/atac-v2.1.0       gurobi/8.1.1                  lib/openblas/0.2.20-gnu                                         pgi/18.10_no_pgi_mpi      
cellranger/v5.0.0            gurobi/9.0.3                  lib/openblas/0.3.5-gnu                                          pgi/18.10_pgi_mpi         
cellranger/v6.1.2            gurobi/11.0.3                 lib/openblas/0.3.13-gnu                                         poppler/0.78.0            
cellranger/v7.0.1            gurobi/11.0.3-server          lib/openblas/0.3.23-gnu                                         proot/5.2.0               
cellranger/v8.0.1            imagemagick/7.0.7-28          lib/openblas/0.3.28                                             psuade/1.7.8              
cesm/2.1.1                   imp/2.10.1-gnu730             lib/openjpeg/2.3.1                                              python/3.10.4             
cesm/2.1.3                   intel-mpi/5.1.3.223           lib/proj/9.5.0                                                  python/3.12.5             
cmake/3.13.4                 intel-mpi/2019.3              lib/readline/6.3                                                qt/5.6.0                  
cmake/3.14.5                 intel/2018.2                  lib/v8/3.14.5                                                   qwt/6.1.5                 
cmake/3.17.3                 intel/2019.3                  lib/volpack/1.0b3                                               R/3.5.3                   
cmake/3.30.1                 intel/2021.4                  lib/vtk/6.3.0                                                   R/3.6.2                   
cmg/2018.101                 java/openjdk-11.0.2           lib/vtk/7.1.1                                                   R/4.2.0                   
cmg/2022.101                 java/openjdk-23.0.1           lib/xerces-c/3.2.2                                              R/4.3.1                   
conda/base                   julia/0.6.3                   lib/zlib/1.2.11                                                 R/4.4.1                   
cp2k/7.1-legacy              julia/1.1.0                   libpq/12.4                                                      rclone/1.53.1             
cp2k/7.1-skylake             julia/1.6.3                   liggghts/20190321_gnu485_opa312                                 rstudio-server/1.4.1103   
cpmd/4.3                     julia/1.11.3                  mathematica/11.0.1                                              rstudio/1.4.1103          
cuda/5.0.35                  kallisto/0.46.1               matlab/r2017b                                                   sage/9.1                  
cuda/8.0.61.2                lammps/12Dec18_gnu485_opa312  matlab/r2018a                                                   singularity/3.4.1         
cuda/10.0.130                lammps/2022-07-23-static      matlab/r2019b                                                   singularity/3.8.1         
cuda/11.3.0                  lib/atlas/3.10.3-gnu          matlab/r2020a                                                   sleuth/0.30.0             
cuda/12.1.1                  lib/beagle/2020-10-27         matlab/r2023a                                                   slim/20190103             
cuda/12.4.1                  lib/boost/1.58.0-mpi          maven/3.6.3                                                     spaceranger/v1.2.1        
cuda/12.6.2                  lib/boost/1.62.0-mpi          minc/1.9.15                                                     spaceranger/v3.1.2        
curl/8.11.1                  lib/boost/1.70.0-mpi          module-git                                                      spack/2024-09-04          
dot                          lib/cgal/4.13.1               module-info                                                     spack/2024-09-04.bak      
dragen-decompression/v2.6.1  lib/cudnn/9.7.1-cuda12        modules                                                         spark/3.2.0               
easybuild/4.9.4              lib/eigen/3.3.4               molden/5.9.2                                                    spark/jupyterhub          
eclipse/2019.1               lib/eigen/3.4.0               mono/5.12                                                       sumo/2020-02-20           
ensembl-api/109              lib/fftw/2.1.5-gnu            mpich/3.2.1-gnu                                                 svn/1.10.6                
ensembl-api/110              lib/fftw/2.1.5-gnu-float      mpich/3.2.1-opa                                                 swig/3.0.12               
espresso/6.3-gnu             lib/fftw/3.3.7-gnu            mpich/3.4.3-gnu                                                 swig/4.0.2                
espresso/7.2                 lib/fftw/3.3.9-gnu            mrtrix/3.0                                                      tcl/8.6.14                
faststructure/2022-04-26     lib/fftw/3.3.10               mrtrix/3.0.4                                                    tesseract-ocr/4.0.0       
ffmpeg/5.0                   lib/gdal/3.9.2                mrtrix3tissue/5.2.9                                             tnavigator/2020-03-04     
fsl/6.0.0                    lib/geos/3.13.0               mysql/8.0.30                                                    tools/cmake/3.10.2        
fsl/6.0.0-bin                lib/gmp/6.2.1                 nco/4.9.2                                                       tools/imagemagick/6.9.9   
fsl/6.0.4                    lib/gsl/2.3                   null                                                            tools/imagemagick/7.0.7   
gams/25.1                    lib/gsl/2.7.1                 nvhpc/nvhpc-byo-compiler_21.7                                   uofl/amber/18             

----------------------------------------------------------------------------------- /work/ebg_lab/software/ebg_modulefiles ------------------------------------------------------------------------------------
aragorn/v1.2.36          guppy/3.6.1           miniconda3/augustus/3.3.3      miniconda3/eukrep           miniconda3/metabat2       miniconda3/repeatmodeler  repeatscout/1.0.6              
bbmap/38.84              guppy/4.0.11          miniconda3/bamtools            miniconda3/fastani          miniconda3/miniasm        miniconda3/samtools       rmblast/2.10.0                 
blast/2.10.0             hmmer/v3.3            miniconda3/bioconductor-dada2  miniconda3/fastqc           miniconda3/minipolish     miniconda3/scapp          signalp/v4.1                   
bwa/0.7.17               mafft/v7.475          miniconda3/bowtie2             miniconda3/flye             miniconda3/nanopolish     minpath/1.4               signalp/v5.0b                  
diamond/v2.0.6           mash/2.2              miniconda3/busco/4.1.4         miniconda3/gtdbtk           miniconda3/nanostat       mothur/1.44.1             snp/snp                        
ebg_java/11.0.1          megahit/1.2.9         miniconda3/checkm              miniconda3/h5py             miniconda3/phylip         prodigal/v2.6.3           SPAdes/3.14.1                  
ebg_perl/5.32.0          metaerg/1.2.0         miniconda3/concoct             miniconda3/maker/2.31.10    miniconda3/porechop       raxml/8.2.12              SURPI-plus-dist/v_march4_2019  
ebg_perl_modules/5.32.0  minced/0.4.2          miniconda3/cutadapt            miniconda3/mamba/4.8.3      miniconda3/python/2.7.15  recon/1.08                tmhmm/2.0c                     
fasttree/2.1.11          miniconda3/4.8.3      miniconda3/das_tool            miniconda3/mamba/snakemake  miniconda3/python/3.9.1   repeatmasker/4.1.1        trf/4.09                       
GeneMark/GeneMark-ES/v4  miniconda3/antismash  miniconda3/drep/3.0.0          miniconda3/maxbin2          miniconda3/racon          repeatmodeler/2.0.1       

Key:
modulepath  default-version  
(base) [ruchita.solanki@arc PL4]$ z
(base) [ruchita.solanki@arc ~]$ conda create -n new_env
Channels:
 - bioconda
 - ursky
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/ruchita.solanki/miniconda3/envs/new_env



Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate new_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) [ruchita.solanki@arc ~]$ conda create -n new_env
WARNING: A conda environment already exists at '/home/ruchita.solanki/miniconda3/envs/new_env'

Remove existing environment?
This will remove ALL directories contained within this specified prefix directory, including any other conda environments.

 (y/[n])? n


CondaSystemExit: Exiting.

(base) [ruchita.solanki@arc ~]$ conda activate new_env
(new_env) [ruchita.solanki@arc ~]$ conda install pandas
Channels:
 - bioconda
 - ursky
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/ruchita.solanki/miniconda3/envs/new_env

  added / updated specs:
    - pandas


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    numpy-2.2.5                |  py313h17eae1a_0         8.1 MB  conda-forge
    pandas-2.2.3               |  py313ha87cce1_3        14.7 MB  conda-forge
    pip-25.1.1                 |     pyh145f28c_0         1.2 MB  conda-forge
    python_abi-3.13            |          7_cp313           7 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        24.1 MB

The following NEW packages will be INSTALLED:

  _libgcc_mutex      conda-forge/linux-64::_libgcc_mutex-0.1-conda_forge 
  _openmp_mutex      conda-forge/linux-64::_openmp_mutex-4.5-2_gnu 
  bzip2              conda-forge/linux-64::bzip2-1.0.8-h4bc722e_7 
  ca-certificates    conda-forge/noarch::ca-certificates-2025.4.26-hbd8a1cb_0 
  ld_impl_linux-64   conda-forge/linux-64::ld_impl_linux-64-2.43-h712a8e2_4 
  libblas            conda-forge/linux-64::libblas-3.9.0-31_h59b9bed_openblas 
  libcblas           conda-forge/linux-64::libcblas-3.9.0-31_he106b2a_openblas 
  libexpat           conda-forge/linux-64::libexpat-2.7.0-h5888daf_0 
  libffi             conda-forge/linux-64::libffi-3.4.6-h2dba641_1 
  libgcc             conda-forge/linux-64::libgcc-15.1.0-h767d61c_2 
  libgcc-ng          conda-forge/linux-64::libgcc-ng-15.1.0-h69a702a_2 
  libgfortran        conda-forge/linux-64::libgfortran-15.1.0-h69a702a_2 
  libgfortran5       conda-forge/linux-64::libgfortran5-15.1.0-hcea5267_2 
  libgomp            conda-forge/linux-64::libgomp-15.1.0-h767d61c_2 
  liblapack          conda-forge/linux-64::liblapack-3.9.0-31_h7ac8fdf_openblas 
  liblzma            conda-forge/linux-64::liblzma-5.8.1-hb9d3cd8_1 
  libmpdec           conda-forge/linux-64::libmpdec-4.0.0-h4bc722e_0 
  libopenblas        conda-forge/linux-64::libopenblas-0.3.29-pthreads_h94d23a6_0 
  libsqlite          conda-forge/linux-64::libsqlite-3.49.2-hee588c1_0 
  libstdcxx          conda-forge/linux-64::libstdcxx-15.1.0-h8f9b012_2 
  libuuid            conda-forge/linux-64::libuuid-2.38.1-h0b41bf4_0 
  libzlib            conda-forge/linux-64::libzlib-1.3.1-hb9d3cd8_2 
  ncurses            conda-forge/linux-64::ncurses-6.5-h2d0b736_3 
  numpy              conda-forge/linux-64::numpy-2.2.5-py313h17eae1a_0 
  openssl            conda-forge/linux-64::openssl-3.5.0-h7b32b05_1 
  pandas             conda-forge/linux-64::pandas-2.2.3-py313ha87cce1_3 
  pip                conda-forge/noarch::pip-25.1.1-pyh145f28c_0 
  python             conda-forge/linux-64::python-3.13.3-hf636f53_101_cp313 
  python-dateutil    conda-forge/noarch::python-dateutil-2.9.0.post0-pyhff2d567_1 
  python-tzdata      conda-forge/noarch::python-tzdata-2025.2-pyhd8ed1ab_0 
  python_abi         conda-forge/noarch::python_abi-3.13-7_cp313 
  pytz               conda-forge/noarch::pytz-2025.2-pyhd8ed1ab_0 
  readline           conda-forge/linux-64::readline-8.2-h8c095d6_2 
  six                conda-forge/noarch::six-1.17.0-pyhd8ed1ab_0 
  tk                 conda-forge/linux-64::tk-8.6.13-noxft_h4845f30_101 
  tzdata             conda-forge/noarch::tzdata-2025b-h78e105d_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                              
Preparing transaction: done                                                                                                                                   
Verifying transaction: done                                                                                 Executing transaction: done                       
(new_env) [ruchita.solanki@arc ~]$ conda install openpyxl                                                                                                     
Channels:
 - bioconda
 - ursky
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/ruchita.solanki/miniconda3/envs/new_env

  added / updated specs:
    - openpyxl


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    et_xmlfile-2.0.0           |     pyhd8ed1ab_1          21 KB  conda-forge
    openpyxl-3.1.5             |  py313h9c9eb82_1         472 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         494 KB

The following NEW packages will be INSTALLED:

  et_xmlfile         conda-forge/noarch::et_xmlfile-2.0.0-pyhd8ed1ab_1 
  openpyxl           conda-forge/linux-64::openpyxl-3.1.5-py313h9c9eb82_1 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                     
Preparing transaction: done                                                                                                                                          
Verifying transaction: done
Executing transaction: done
(new_env) [ruchita.solanki@arc ~]$ z RS
-bash: zoxide: command not found
(new_env) [ruchita.solanki@arc ~]$ cd /work/ebg_lab/gm/RS/metatranscriptomics/PL4
-bash: zoxide: command not found
(new_env) [ruchita.solanki@arc PL4]$ ls
RS-PL4-1-RNA_S15_L001_R1_001.fastq.gz  RS-PL4-2-RNA_S16_L002_R2_001.fastq.gz  sealrpkm_RS-PL4-1-RNA_S15_R1.txt   sealstats_RS-PL4-2-RNA_S16_R1.txt
RS-PL4-1-RNA_S15_L001_R2_001.fastq.gz  RS-PL4-2-RNA_S16_R1_merged.fastq.gz    sealrpkm_RS-PL4-1-RNA_S15_R2.txt   sealstats_RS-PL4-2-RNA_S16_R2.txt
RS-PL4-1-RNA_S15_L002_R1_001.fastq.gz  RS-PL4-2-RNA_S16_R2_merged.fastq.gz    sealrpkm_RS-PL4-2-RNA_S16_R1.txt   sealstats_RS-PL4-3-RNA_S17_R1.txt
RS-PL4-1-RNA_S15_L002_R2_001.fastq.gz  RS-PL4-3-RNA_S17_L001_R1_001.fastq.gz  sealrpkm_RS-PL4-2-RNA_S16_R2.txt   sealstats_RS-PL4-3-RNA_S17_R2.txt
RS-PL4-1-RNA_S15_R1_merged.fastq.gz    RS-PL4-3-RNA_S17_L001_R2_001.fastq.gz  sealrpkm_RS-PL4-3-RNA_S17_R1.txt   slurm-34970905.out
RS-PL4-1-RNA_S15_R2_merged.fastq.gz    RS-PL4-3-RNA_S17_L002_R1_001.fastq.gz  sealrpkm_RS-PL4-3-RNA_S17_R2.txt   tpm_calculator.py
RS-PL4-2-RNA_S16_L001_R1_001.fastq.gz  RS-PL4-3-RNA_S17_L002_R2_001.fastq.gz  seal.sbatch                        tpm_calculator_v1.py
RS-PL4-2-RNA_S16_L001_R2_001.fastq.gz  RS-PL4-3-RNA_S17_R1_merged.fastq.gz    sealstats_RS-PL4-1-RNA_S15_R1.txt
RS-PL4-2-RNA_S16_L002_R1_001.fastq.gz  RS-PL4-3-RNA_S17_R2_merged.fastq.gz    sealstats_RS-PL4-1-RNA_S15_R2.txt
(new_env) [ruchita.solanki@arc PL4]$ python3 tpm_calculator.py 
TPM results saved to /work/ebg_lab/gm/RS/metatranscriptomics/PL4/tpm_all.xlsx
Done.
(new_env) [ruchita.solanki@arc PL4]$ ls
RS-PL4-1-RNA_S15_L001_R1_001.fastq.gz  RS-PL4-2-RNA_S16_L002_R2_001.fastq.gz  sealrpkm_RS-PL4-1-RNA_S15_R1.txt   sealstats_RS-PL4-2-RNA_S16_R1.txt
RS-PL4-1-RNA_S15_L001_R2_001.fastq.gz  RS-PL4-2-RNA_S16_R1_merged.fastq.gz    sealrpkm_RS-PL4-1-RNA_S15_R2.txt   sealstats_RS-PL4-2-RNA_S16_R2.txt
RS-PL4-1-RNA_S15_L002_R1_001.fastq.gz  RS-PL4-2-RNA_S16_R2_merged.fastq.gz    sealrpkm_RS-PL4-2-RNA_S16_R1.txt   sealstats_RS-PL4-3-RNA_S17_R1.txt
RS-PL4-1-RNA_S15_L002_R2_001.fastq.gz  RS-PL4-3-RNA_S17_L001_R1_001.fastq.gz  sealrpkm_RS-PL4-2-RNA_S16_R2.txt   sealstats_RS-PL4-3-RNA_S17_R2.txt
RS-PL4-1-RNA_S15_R1_merged.fastq.gz    RS-PL4-3-RNA_S17_L001_R2_001.fastq.gz  sealrpkm_RS-PL4-3-RNA_S17_R1.txt   slurm-34970905.out
RS-PL4-1-RNA_S15_R2_merged.fastq.gz    RS-PL4-3-RNA_S17_L002_R1_001.fastq.gz  sealrpkm_RS-PL4-3-RNA_S17_R2.txt   tpm_all.xlsx
RS-PL4-2-RNA_S16_L001_R1_001.fastq.gz  RS-PL4-3-RNA_S17_L002_R2_001.fastq.gz  seal.sbatch                        tpm_calculator.py
RS-PL4-2-RNA_S16_L001_R2_001.fastq.gz  RS-PL4-3-RNA_S17_R1_merged.fastq.gz    sealstats_RS-PL4-1-RNA_S15_R1.txt  tpm_calculator_v1.py
RS-PL4-2-RNA_S16_L002_R1_001.fastq.gz  RS-PL4-3-RNA_S17_R2_merged.fastq.gz    sealstats_RS-PL4-1-RNA_S15_R2.txt
(new_env) [ruchita.solanki@arc PL4]$ less tpm_all.xlsx
"tpm_all.xlsx" may be a binary file.  See it anyway? 
(new_env) [ruchita.solanki@arc PL4]$ 
(new_env) [ruchita.solanki@arc PL4]$ pwd
/work/ebg_lab/gm/RS/metatranscriptomics/PL4
(new_env) [ruchita.solanki@arc PL4]$ rm tpm_all.xlsx
(new_env) [ruchita.solanki@arc PL4]$ nano tpm_calculator.py
(new_env) [ruchita.solanki@arc PL4]$ 
(new_env) [ruchita.solanki@arc PL4]$ less tpm_calculator.py

    Processes all relevant files in the given directory to calculate TPM and
    merges the results into a single DataFrame.

    Args:
        directory (str): Path to the directory containing the input files.

    Returns:
        pandas.DataFrame: A DataFrame containing TPM values for all processed samples,
                          or None if no valid files were found.
    """
    all_results = []
    for filename in os.listdir(directory):
        if filename.startswith("sealrpkm_") and filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            result_df = calculate_tpm(filepath)
            if result_df is not None:  # Only process valid files
                sample_name = os.path.splitext(filename)[0]
                result_df = result_df.rename(columns={'TPM': sample_name})
                all_results.append(result_df)

    if not all_results:
        print("No valid 'sealrpkm_*.txt' files found to process.")
        return None

    # Merge all DataFrames on '#Name'
    tpm_all = all_results[0]
    for df in all_results[1:]:
        tpm_all = pd.merge(tpm_all, df, on='#Name', how='outer')
    tpm_all = tpm_all.fillna(0)  # Fill NaN values with 0
    return tpm_all

def save_results(df, output_path):
    """
    Saves the given DataFrame to an Excel file.

    Args:
        df (pandas.DataFrame): The DataFrame to save.
        output_path (str): Path to the output Excel file.
    """
    try:
        df.to_excel(output_path, index=False)
        print(f"TPM results saved to {output_path}")
    except Exception as e:
        print(f"Error saving to Excel: {e}")

if __name__ == "__main__":
    work_dir = os.path.dirname(os.path.abspath(__file__))  # Use current directory
    # If you want to use a specific directory, uncomment and modify the line below.
    # work_dir = r"D:\OneDrive - University of Calgary\Exp_Sediment\Experiments\Molecular_biology\2025_Apr\seal"

    tpm_all_df = process_files(work_dir)
    if tpm_all_df is not None:
        tpm_all_path = os.path.join(work_dir, "tpm_all.xlsx")
        save_results(tpm_all_df, tpm_all_path)
    print("Done.")
