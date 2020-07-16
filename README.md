# L1TauProducerPhase2

# To run in CMSSW_11_1_0


cmsrel CMSSW_11_1_0

cd CMSSW_11_1_0/src

cmsenv

git cms-init



# To Reconstruct L1 HPS Tau

git cms-addpkg DataFormats/L1TCorrelator

cp /home/sbhowmik/HLTTau/HLTTauProducerPhase2/CMSSW_11_1_0/src/DataFormats/L1TCorrelator/interface/TkPrimaryVertex.h $CMSSW_BASE/src/DataFormats/L1TCorrelator/interface

cp /home/sbhowmik/HLTTau/HLTTauProducerPhase2/CMSSW_11_1_0/src/DataFormats/L1TCorrelator/src/classes_def.xml $CMSSW_BASE/src/DataFormats/L1TCorrelator/src


git cms-addpkg DataFormats/L1Trigger

cp /home/sbhowmik/HLTTau/HLTTauProducerPhase2/CMSSW_11_1_0/src/DataFormats/L1Trigger/interface/Muon.h $CMSSW_BASE/src/DataFormats/L1Trigger/interface

cp /home/sbhowmik/HLTTau/HLTTauProducerPhase2/CMSSW_11_1_0/src/DataFormats/L1Trigger/src/classes_def.xml $CMSSW_BASE/src/DataFormats/L1Trigger/src



git clone https://github.com/sandeepbhowmik1/L1TauProducerPhase2 $CMSSW_BASE/src/L1Trigger/Phase2L1Taus 

git clone https://github.com/sandeepbhowmik1/L1TauProducerPhase2-DataFormats $CMSSW_BASE/src/DataFormats/Phase2L1Taus


scram b -j 8




# To Reconstruct HLT Tau

git cms-addpkg FastSimulation/Event

git remote add hatakeyamak https://github.com/hatakeyamak/cmssw.git

git fetch hatakeyamak

git cherry-pick 0cf67551731c80dc85130e4b8ec73c8f44d53cb0


git cms-merge-topic veelken:CMSSW_11_1_x_maxDeltaZToLeadTrack


git clone https://github.com/HEP-KBFI/hlttrigger-phase2hltpftaus $CMSSW_BASE/src/HLTrigger/Phase2HLTPFTaus

git clone https://github.com/HEP-KBFI/dataformats-phase2hltpftaus $CMSSW_BASE/src/DataFormats/Phase2HLTPFTaus

git clone https://github.com/veelken/hlttrigger-phase2hltpftauanalyzer $CMSSW_BASE/src/HLTrigger/TallinnHLTPFTauAnalyzer

git clone https://github.com/veelken/l1trigger-phase2l1pftauanalyzer $CMSSW_BASE/src/L1Trigger/TallinnL1PFTauAnalyzer

git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2

scram b -j 8



# To Produce L1 and HLT Tau in a same file

cp /home/sbhowmik/HLTTau/HLTTauProducerPhase2/CMSSW_11_1_0/src/L1Trigger/Phase2L1Taus/test/hltPhase2_MINBIAS_TRKv06_TICL_withTaus_andL1_copy_cfg.py $CMSSW_BASE/src/L1Trigger/Phase2L1Taus/test


scram b -j 8



cmsRun $CMSSW_BASE/src/L1Trigger/Phase2L1Taus/test/hltPhase2_MINBIAS_TRKv06_TICL_withTaus_andL1_copy_cfg.py


