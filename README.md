# L1TauProducerPhase2

# To run in CMSSW_11_1_0


cmsrel CMSSW_11_1_0

cd CMSSW_11_1_0/src

cmsenv

git cms-init


git cms-addpkg DataFormats/L1TCorrelator


......................................................................

modify

DataFormats/L1TCorrelator/interface/TkPrimaryVertex.h

add:

typedef edm::Ref<TkPrimaryVertexCollection> TkPrimaryVertexRef;


modify

DataFormats/L1TCorrelator/src/classes_def.xml

add:

class name="l1t::TkPrimaryVertexRef"/

class name="edm::Wrapper<l1t::TkPrimaryVertexRef>"/

.....................................................................


git cms-addpkg DataFormats/L1Trigger


.....................................................................

modify

DataFormats/L1Trigger/interface/Muon.h

add:

typedef edm::Ptr<Muon> MuonPtr;

inline void setTfMuonIndex(int index_) { tfMuonIndex_ = index_; };


modify

DataFormats/L1Trigger/src/classes_def.xml

add:

class name="l1t::MuonPtr"/

class name="edm::Wrapper<l1t::MuonPtr>"/

.....................................................................


git clone https://github.com/sandeepbhowmik1/L1TauProducerPhase2

mv L1TauProducerPhase2/DataFormats/* DataFormats/

mv L1TauProducerPhase2/L1Trigger .


scram b -j 8





