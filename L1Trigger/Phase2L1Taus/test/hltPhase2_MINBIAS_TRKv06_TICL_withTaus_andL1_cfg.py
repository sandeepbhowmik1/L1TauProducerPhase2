# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --geometry Extended2026D49 --era Phase2C9 --conditions auto:phase2_realistic_T15 --processName RECO2 --step RAW2DIGI,RECO --eventcontent RECO --datatier RECO --filein /store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/8A31EE8B-FC0F-A949-8340-58E2ABD2F30F.root --mc --nThreads 4 --nStreams 4 --no_exec -n 10 --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring --customise JMETriggerAnalysis/Common/hltPhase2_TRKv06.customize_hltPhase2_TRKv06 --customise JMETriggerAnalysis/Common/hltPhase2_JME.customize_hltPhase2_JME --customise JMETriggerAnalysis/Common/hltPhase2_JME.customize_hltPhase2_TICL --customise_commands process.schedule.remove(process.RECOoutput_step)\ndel process.RECOoutput\ndel process.RECOoutput_step\n --python_filename hltPhase2_MINBIAS_TRKv06_TICL_NoskimmedTracks_cfg.py
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('RECO2',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#--------------------------------------------------------------------------------
# CV: switch between offline-like and Pixel vertices

vertices = "OfflineVertices"
#vertices = "OnlineVertices"
#vertices = "OnlineVerticesTrimmed"

srcVertices = None
if vertices == "OfflineVertices":
    srcVertices = "offlinePrimaryVertices"
elif vertices == "OnlineVertices":
    srcVertices = "hltPhase2PixelVertices"
elif vertices == "OnlineVerticesTrimmed":
    srcVertices = "hltPhase2TrimmedPixelVertices"
else:
    raise ValueError("Invalid configuration parameter vertices = '%s' !!" % vertices)
#--------------------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20RECOMiniAOD/MinBias_TuneCP5_14TeV-pythia8/MINIAODSIM/PU200_110X_mcRun4_realistic_v3-v1/110000/054D8F53-89B2-E143-B106-FD85AC2F1F4B.root'
    ),
    secondaryFileNames = cms.untracked.vstring(
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/8A31EE8B-FC0F-A949-8340-58E2ABD2F30F.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/7CD16EEB-247E-A340-9C46-6345ECF18A82.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/7795313D-A909-354A-9226-41B90CDCF847.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/6920F67D-2E85-7D4E-835D-C7B76479E559.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/56CB55A4-4E1C-F04B-8693-FD79CD1D5986.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/49726925-BB46-304E-B1C5-8518C1CB2BDB.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/46BDEEBE-B254-E044-B0BA-CF5C030D564A.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/4497DDB7-BE79-D047-9CAF-05A5FF96D4B4.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/87F38519-6E6B-9444-836C-9597AA3152A2.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/061AB47E-D89E-C14B-9948-7CDB3367BD9B.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/1BE20D65-DC91-984B-9892-215E72AB5757.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/1EC9A6C4-23A7-C048-9182-9E8FB7ED942A.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110001/3C2BDEAE-6D19-3A48-9AC8-6BC2F555DF1F.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/0E00FF93-32FF-FD4C-989F-3A0C5FA653C1.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/534D3139-A254-E24B-A125-3C176575E2DB.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/B6EDAEB7-BCF6-004C-AD7C-114ED961F96B.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/2F2FD1CF-BC4E-C446-BA43-A55DFD616495.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/B67BDC43-0F45-4A4A-B97C-B4926D262C9F.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/E3B48CFD-B0AA-D04E-958A-472D3BD7C5E7.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/BD8132F5-E3F5-2C4D-BD6A-6FD057E77122.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/A62403FD-AFBC-3D47-BCE6-DE8F9594CA6F.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/6F3F0A0A-59A1-7D49-B4BC-E11A4F662A67.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/4F3FFE77-9E3A-0B43-A2F5-546EF6F69552.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/C235BF90-10BE-AB48-A717-A9BD1625EA5B.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/A8D780B8-0E4B-A44E-96AF-CEBFA2A39EDF.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/B4758DB4-B280-9445-9E8D-B852B73391EC.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/8A65476E-E45D-E04B-95F9-66800ACA1714.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/89426CC6-3809-9E45-A578-E64C2E7D3B07.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/B59E0FE9-CE72-7E43-A814-5FE7DD15E854.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/BE759C01-AE6C-A84B-BA93-E76BD7D6F016.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/A58A5451-981C-1447-96CD-8B9C5C734024.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/ECF64A08-DAA8-1D47-86CE-3B1F630372A2.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/4BCFDBF1-7692-5B45-AFAD-740E349A1B5F.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/EDADE3F7-34D0-5544-A61F-BCF27308D5D9.root',
        'file:/hdfs/cms/store/mc/Phase2HLTTDRWinter20DIGI/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v1/110002/381C2BBE-366A-384E-97AF-BFF7AAFD8C9E.root'
    )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(8),
    numberOfThreads = cms.untracked.uint32(8),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)

# Output definition
process.RECOoutput = cms.OutputModule("PoolOutputModule",
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('step3_RAW2DIGI_RECO.root'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('reconstruction_step')
    ),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ak4GenJets*_*_*',                   ## PRESENT ONLY IN RAW
        'keep *_hltGtStage2Digis*_*_*',             ## PRESENT ONLY IN RAW
        'keep *_hltTriggerSummaryRAW*_*_*',         ## PRESENT ONLY IN RAW
        'keep *_ak4PFJetsCorrected*_*_*',           ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_hlt*Tau*_*_*',                      ## PRODUCED BY addHLTPFTaus FUNCTION BELOW
        'keep *_particleFlowTmp_*_*',               ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_muons1stStep_*_*',                  ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_electronGsfTracks_*_*',             ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_generalTracks_*_*',                 ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_offlinePrimaryVertices_*_*',        ## KEEP REFERENCE TO reco::PFCandidate COLLECTION GIVEN AS INPUT TO addHLTPFTaus FUNCTION
        'keep *_hltPhase2PixelVertices_*_*',        ## PRODUCED BELOW
        'keep *_hltPhase2TrimmedPixelVertices_*_*', ## PRODUCED BELOW
        'keep *_hltKT6PFJets_*_*',                  ## PRODUCED BELOW
        'keep *_prunedGenParticles_*_*',            ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_ak4GenJets_*_*',                    ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_ak8GenJets_*_*',                    ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_slimmedGenJets__*',                 ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_slimmedTaus_*_*',                   ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_slimmedJets_*_*',                   ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_packedPFCandidates_*_*',            ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_slimmedAddPileupInfo_*_*',          ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_offlineSlimmedPrimaryVertices_*_*', ## PRESENT ONLY IN MINIAOD/RECO
        'keep *_generatorSmeared_*_*',              ## CV: ALLOWS TO PRODUCE FULL COLLECTION OF genParticles FOR DEBUGGING PURPOSES 
        'keep *_L1HPSPFTauProducer*PF_*_*',         ## ADDED BY L1 EMULATOR
        'keep *_l1pfCandidates_PF_*',               ## ADDED BY L1 EMULATOR
        'keep *_l1pfProducer*_z0_*',                ## ADDED BY L1 EMULATOR
        'keep *_pfTracksFromL1Tracks*_*_*',         ## ADDED BY L1 EMULATOR
        'keep *_pfClustersFrom*_*_*',               ## ADDED BY L1 EMULATOR 
        'keep *_TTTracksFromTracklet_*_*',          ## ADDED BY L1 EMULATOR
        'keep *_VertexProducer_*_*',                ## ADDED BY L1 EMULATOR
        'keep *_ak4PFL1PF_*_*',                     ## ADDED BY L1 EMULATOR
        'keep *_ak4PFL1PFCorrected_*_*',            ## ADDED BY L1 EMULATOR
        'keep *_kt6L1PFJetsPF_rho_*',               ## ADDED BY L1 EMULATOR
        'keep *_kt6L1PFJetsNeutralsPF_rho_*',       ## ADDED BY L1 EMULATOR        
        'keep *_l1pfCandidates_PF_*',
        'keep *_l1pfCandidates_Puppi_*',
        'keep *_L1TkPrimaryVertex_*_*',
        'keep *_L1HPSPFTauProducer*PF_*_*',
        'keep *_L1HPSPFTauProducer*Puppi_*_*',
        'keep *_prunedGenParticles_*_*',
        'keep *_tauGenJetsSelectorAllHadrons_*_*',
        'keep *_generator_*_*',
    )
)

process.RECOoutput_step = cms.EndPath(process.RECOoutput)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from JMETriggerAnalysis.Common.hltPhase2_TRKv06
from JMETriggerAnalysis.Common.hltPhase2_TRKv06 import customize_hltPhase2_TRKv06 

#call to customisation function customize_hltPhase2_TRKv06 imported from JMETriggerAnalysis.Common.hltPhase2_TRKv06
process = customize_hltPhase2_TRKv06(process)

# Automatic addition of the customisation function from JMETriggerAnalysis.Common.hltPhase2_JME
from JMETriggerAnalysis.Common.hltPhase2_JME import customize_hltPhase2_JME,customize_hltPhase2_TICL 

#call to customisation function customize_hltPhase2_JME imported from JMETriggerAnalysis.Common.hltPhase2_JME
process = customize_hltPhase2_JME(process)

#call to customisation function customize_hltPhase2_TICL imported from JMETriggerAnalysis.Common.hltPhase2_JME
process = customize_hltPhase2_TICL(process)

#--------------------------------------------------------------------------------
# CV: run HLT Pixel vertex reconstruction
process.load("HLTTrigger.Phase2HLTPFTaus.hltPixelVertices_cff")
process.reconstruction_step.replace(process.offlinePrimaryVertices, process.offlinePrimaryVertices + process.hltPhase2PixelTracksSequence + process.hltPhase2PixelVerticesSequence)

# CV: switch vertex collection in particle-flow algorithm
if srcVertices != "offlinePrimaryVertices":
    print("Switching all vertex-related InputTags in 'reconstruction_step' path from '%s' to '%s'..." % ('offlinePrimaryVertices', srcVertices))
    from FWCore.ParameterSet.MassReplace import massSearchReplaceAnyInputTag
    massSearchReplaceAnyInputTag(process.reconstruction_step, 'offlinePrimaryVertices', srcVertices)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# CV: add HLT tau reconstruction
process.taucustomreco = cms.Sequence()

# run HLT tau reconstruction
from HLTTrigger.Phase2HLTPFTaus.tools.addHLTPFTaus import addHLTPFTaus
srcPFCandidates = "particleFlowTmp"
for algorithm in [ "hps", "shrinking-cone" ]:
    for isolation_maxDeltaZOption in [ "primaryVertex", "leadTrack" ]:
      for isolation_minTrackHits in [ 3, 5, 8 ]:  

        suffix = "%iHits" % isolation_minTrackHits
        isolation_maxDeltaZ            = None
        isolation_maxDeltaZToLeadTrack = None
        if isolation_maxDeltaZOption == "primaryVertex":
          isolation_maxDeltaZ            =  0.15 # value optimized for offline tau reconstruction at higher pileup expected during LHC Phase-2
          isolation_maxDeltaZToLeadTrack = -1.   # disabled
          suffix += "MaxDeltaZ"
        elif isolation_maxDeltaZOption == "leadTrack":
          isolation_maxDeltaZ            = -1.   # disabled
          isolation_maxDeltaZToLeadTrack =  0.15 # value optimized for offline tau reconstruction at higher pileup expected during LHC Phase-2
          suffix += "MaxDeltaZToLeadTrack"
        else:
          raise ValueError("Invalid parameter isolation_maxDeltaZOption = '%s' !!" % isolation_maxDeltaZOption)
        if srcVertices == "offlinePrimaryVertices":
          suffix += "WithOfflineVertices"
        elif srcVertices == "hltPhase2PixelVertices":
          suffix += "WithOnlineVertices"
        elif srcVertices == "hltPhase2TrimmedPixelVertices":
          suffix += "WithOnlineVerticesTrimmed"
        else:
          raise ValueError("Invalid parameter srcVertices = '%s' !!" % srcVertices)        
        
        pftauSequence = addHLTPFTaus(process, algorithm, srcPFCandidates, srcVertices, 
          isolation_maxDeltaZ, isolation_maxDeltaZToLeadTrack, isolation_minTrackHits, 
          suffix)
        process.taucustomreco += pftauSequence

process.reconstruction_step += process.taucustomreco

# CV: add kt6PFJets for rho computation
from RecoJets.JetProducers.kt6PFJets_cfi import kt6PFJets
process.hltKT6PFJets = kt6PFJets.clone(
    src = cms.InputTag("particleFlowTmp"),
    doRhoFastjet = cms.bool(True)
)
process.reconstruction_step += process.hltKT6PFJets

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# CV: add L1 trigger emulator

process.l1emulator = cms.Sequence()

process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')
process.load('CalibCalorimetry.CaloTPG.CaloTPGTranscoder_cfi')

process.load('L1Trigger.L1THGCal.hgcalTriggerPrimitives_cff')
process.l1emulator += process.hgcalTriggerPrimitives

process.load('SimCalorimetry.EcalEBTrigPrimProducers.ecalEBTriggerPrimitiveDigis_cff')
process.l1emulator += process.simEcalEBTriggerPrimitiveDigis

process.load("L1Trigger.TrackFindingTracklet.Tracklet_cfi")
L1TRK_PROC  =  process.TTTracksFromTrackletEmulation
L1TRK_NAME  = "TTTracksFromTrackletEmulation"
L1TRK_LABEL = "Level1TTTracks"

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cfi")
process.l1emulator += process.offlineBeamSpot

process.l1emulator += process.TTTracksFromTrackletEmulation

process.load("SimTracker.TrackTriggerAssociation.TrackTriggerAssociator_cff")
process.TTTrackAssociatorFromPixelDigis.TTTracks = cms.VInputTag( cms.InputTag(L1TRK_NAME, L1TRK_LABEL) )
process.l1emulator += process.TrackTriggerAssociatorTracks

process.load("L1Trigger.L1TTrackMatch.L1TkPrimaryVertexProducer_cfi")
process.l1emulator += process.L1TkPrimaryVertex

process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.l1emulator += process.SimL1Emulator

process.load("L1Trigger.Phase2L1ParticleFlow.pfTracksFromL1Tracks_cfi")
process.l1emulator += process.pfTracksFromL1Tracks

process.load("L1Trigger.Phase2L1ParticleFlow.l1ParticleFlow_cff")
process.l1emulator += process.l1ParticleFlow

process.load("L1Trigger.Phase2L1ParticleFlow.l1pfJetMet_cff")
process.l1emulator += process.l1PFJets

process.kt6L1PFJetsPF = process.ak4PFL1PF.clone(
    jetAlgorithm = cms.string("Kt"),
    rParam       = cms.double(0.6),
    doRhoFastjet = cms.bool(True),
    Rho_EtaMax   = cms.double(3.0)
)
process.l1emulator += process.kt6L1PFJetsPF
process.l1pfNeutralCandidatesPF = cms.EDFilter("L1TPFCandSelector",
    src = cms.InputTag('l1pfCandidates:PF'),
    cut = cms.string("pdgId = 22"), # CV: cms.string("id = Photon") does not work (does not select any l1t::PFCandidates)                                                                                                                                                       
    filter = cms.bool(False)
)
process.l1emulator += process.l1pfNeutralCandidatesPF
process.kt6L1PFJetsNeutralsPF = process.kt6L1PFJetsPF.clone(
    src = cms.InputTag('l1pfNeutralCandidatesPF')
)
process.l1emulator += process.kt6L1PFJetsNeutralsPF

process.kt6L1PFJetsPuppi = process.kt6L1PFJetsPF.clone(
    src = cms.InputTag('l1pfCandidates:Puppi')
)
process.l1emulator += process.kt6L1PFJetsPuppi
process.l1pfNeutralCandidatesPuppi = process.l1pfNeutralCandidatesPF.clone(
    src = cms.InputTag('l1pfCandidates:Puppi'),
)
process.l1emulator += process.l1pfNeutralCandidatesPuppi
process.kt6L1PFJetsNeutralsPuppi = process.kt6L1PFJetsPuppi.clone(
    src = cms.InputTag('l1pfNeutralCandidatesPuppi')
)
process.l1emulator += process.kt6L1PFJetsNeutralsPuppi

############################################################ 
# Generator-level (visible) hadronic taus  
############################################################ 

process.load("PhysicsTools.JetMCAlgos.TauGenJets_cfi")
#process.tauGenJets.GenParticles = cms.InputTag("prunedGenParticles")                                                                                                                                                                                                           
process.tauGenJets.GenParticles = cms.InputTag("genParticles")

process.load("PhysicsTools.JetMCAlgos.TauGenJetsDecayModeSelectorAllHadrons_cfi")

process.genTaus = cms.Sequence(process.tauGenJets + process.tauGenJetsSelectorAllHadrons)
process.l1emulator += process.genTaus

############################################################
# produce  L1 HPS PF Tau objects 
############################################################   

from L1Trigger.Phase2L1Taus.L1HPSPFTauProducerPF_cfi import L1HPSPFTauProducerPF
from L1Trigger.Phase2L1Taus.L1HPSPFTauProducerPuppi_cfi import L1HPSPFTauProducerPuppi
for useStrips in [ True, False ]:
    moduleNameBase = "L1HPSPFTauProducer"
    if useStrips:
        moduleNameBase += "WithStrips"
    else:
        moduleNameBase += "WithoutStrips"

    moduleNamePF = moduleNameBase + "PF"
    modulePF = L1HPSPFTauProducerPF.clone(
        useStrips = cms.bool(useStrips),
        applyPreselection = cms.bool(False),
        debug = cms.untracked.bool(False)
    )
    setattr(process, moduleNamePF, modulePF)
    process.l1emulator += getattr(process, moduleNamePF)



process.reconstruction_step += process.l1emulator
#--------------------------------------------------------------------------------

# End of customisation functions

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

##dump_file = open('dump.py','w')
##dump_file.write(process.dumpPython())

#Setup FWK for multithreaded
process.options.numberOfThreads = cms.untracked.uint32(8)
process.options.numberOfStreams = cms.untracked.uint32(8)
process.options.numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1)









