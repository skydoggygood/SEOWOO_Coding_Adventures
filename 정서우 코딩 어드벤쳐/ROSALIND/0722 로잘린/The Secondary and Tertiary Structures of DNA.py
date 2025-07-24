# # The Secondary and Tertiary Structures of DNA

# # Problem
# # In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# # The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# # Given: A DNA string s of length at most 1000 bp.

# # Return: The reverse complement sc of s.

# # Sample Dataset
# # AAAACCCGGT

# # Sample Output
# # ACCGGGTTTT

# GATK=/BiO/Access/home/user39/tools/gatk
# java="/BiO/Access/home/user39/tools/jdk-11.0.2/bin/java"
# java17="/BiO/Access/home/user39/tools/jdk-17.0.2/bin/java"
# picard="/BiO/Access/home/user39/tools/picard/picard.jar"
# prefix=Ecoil
# snpeff="/BiO/Access/home/user39/tools/snpeff-5.2-0"
# export PATH=/BiO/Access/home/user39/miniconda3/bin/:$PATH

# # Analysis Preparing

# mkdir PacBio_reseq ; cd PacBio_reseq

# cp /BiO/Access/home/user39/Data/PacBio/PacBio_Rawdata.fastq .
# cp /BiO/Access/home/user39/Data/PacBio/Mapping/Ref.fasta .

# # Reference Indexing

# pbmm2 index Ref.fasta Ref.mmi

# samtools faidx Ref.fasta

# ${java17} -jar ${picard} CreateSequenceDictionary R=Ref.fasta O=Ref.dict

# # Mapping

# pbmm2 align -j 2 --sort --preset CCS Ref.mmi PacBio_Rawdata.fastq mapped.bam

# samtools flagstat mapped.bam > mapped.bam.flagstat

# samtools index mapped.bam

# samtools depth mapped.bam > bam.depth

# # Variants Calling

# ${GATK} HaplotypeCaller -R Ref.fasta -I mapped.bam -O PacBio.g.vcf -ERC GVCF

# ${GATK} GenotypeGVCFs -R Ref.fasta -V PacBio.g.vcf -O rawVariants.vcf

# # SNP / Indel Filtering

# ${GATK} SelectVariants -R Ref.fasta -V rawVariants.vcf --select-type-to-include SNP -O rawSNPs.vcf

# ${GATK} SelectVariants -R Ref.fasta -V rawVariants.vcf --select-type-to-include INDEL -O rawINDELs.vcf

# ${GATK} VariantFiltration -R Ref.fasta -V rawSNPs.vcf -filter "QD < 5.0 || QUAL < 50.0 || DP < 15 || FS > 40.0 || SOR > 2.0 || MQ < 50.0 || MQRankSum < -8.0 || ReadPosRankSum < -5.0" --filter-name 'SNP_Filter' -O rawSNPs.Filtered.vcf

# # SNP / Indel Filtering (2)

# ${GATK} VariantFiltration -R Ref.fasta -V rawINDELs.vcf -filter QD < 5.0 || QUAL < 50.0 || DP < 15 || FS > 100.0 || SOR > 5.0 || ReadPosRankSum <- 10.0' --filter-name'INDEL_Filter' -O rawINDELs.Filtered.vcf
# ${GATK} VariantFiltration -R Ref.fasta -V rawINDELs.vcf -filter "QD < 5.0 || QUAL < 50.0 || DP < 15 || FS > 100.0 || SOR > 5.0 || ReadPosRankSum < -10.0" --filter-name 'INDEL_Filter' -O rawINDELs.Filtered.vcf

# grep ^# rawSNPs.Filtered.vcf > Filtered.vcf

# awk '{if($7=="PASS")print$A}' rawSNPs.Filtered.vcf rawINDELs.Filtered.vcf >> Filtered.vcf

# # Annotation

# ${java} -jar $snpeff/snpEff.jar -v $prefix Filtered.vcf > annotated.vcf

# # SV calling

# pbsv discover mapped.bam mapped.svsig.gz

# pbsv call -j 20 Ref.fasta mapped.svsig.gz.pbsv.vcf

# # 결과확인

# cat mapped.bam.flagstat

# 6236 + 0 in total (QC-passed reads + QC-failed reads)
# 0 + 0 secondary
# 236 + 0 supplementary
# 0 + 0 duplicates
# 6236 + 0 mapped (100.00% : N/A)
# 0 + 0 paired in sequencing
# 0 + 0 read1
# 0 + 0 read2
# 0 + 0 properly paired (N/A : N/A)
# 0 + 0 with itself and mate mapped
# 0 + 0 singletons (N/A : N/A)
# 0 + 0 with mate mapped to a different chr
# 0 + 0 with mate mapped to a different chr (mapQ>=5)

# raw=$(grep -c '^@' PacBio_Rawdata.fastq | awk '{print $1 * 2}')
# filt=$(grep -c '^@' PacBio_Rawdata.fastq | awk '{print $1s * 2}')
# initial=$(cat mapped.bam.flagstat | sed -n '10,11p' | cut -d ' ' -f 1 | awk '{sum+=$1}END{print sum}')
# dedup=$(cat KoreaBio_rmdup.bam.flagstat | sed -n '10,11p' | cut -d ' ' -f 1 | awk '{sum+=$1}END{print sum}')
# types=$(grep -v '^#' annotated.vcf | awk '{if(length($4)==length($5)){SNP+=1}else{INDEL+=1}}END{print SNP+INDEL,SNP,INDEL}')

# deco=$(wc -l bam.depth | cut -d ' ' -f 1)
# gs=$(awk '{if(index($1,">")==0) sum+=length($A)}END{print sum}' Ref/Ref.fasta)

# echo """
# # of Raw reads : ${raw}
# Mapping ratio : $(echo ${initial} ${filt} | awk '{print $1/$2*100 "%"}')
# De-dup ratio : $(echo ${dedup} ${initial} | awk '{print $1/$2*100 "%"}')
# # of Variants : $(echo ${types} | cut -d ' ' -f 1)
# # of SNPs : $(echo ${types} | cut -d ' ' -f 2)
# # of Indels : $(echo ${types} | cut -d ' ' -f 3)
# Genome coverage : $(echo ${deco} ${gs} | awk '{print $1/$2*100 "%"}')
# """

S = input()

S_reverse = S[::-1]

S_reverse = S_reverse.replace("A", "x")
S_reverse = S_reverse.replace("T", "y")
S_reverse = S_reverse.replace("C", "z")
S_reverse = S_reverse.replace("G", "w")

S_reverse = S_reverse.replace("x", "T")
S_reverse = S_reverse.replace("y", "A")
S_reverse = S_reverse.replace("z", "G")
S_reverse = S_reverse.replace("w", "C")

print(S_reverse)
