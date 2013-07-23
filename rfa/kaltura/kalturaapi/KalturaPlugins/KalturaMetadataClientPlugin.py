# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2011  Kaltura Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# @ignore
# ===================================================================================================
# @package External
# @subpackage Kaltura
import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
# @package External
# @subpackage Kaltura
class KalturaMetadataProfileCreateMode:
    API = 1
    KMC = 2
    APP = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaMetadataProfileStatus:
    ACTIVE = 1
    DEPRECATED = 2
    TRANSFORMING = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaMetadataStatus:
    VALID = 1
    INVALID = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaMetadataObjectType:
    AD_CUE_POINT = "adCuePoint.AdCuePoint"
    ANNOTATION = "annotation.Annotation"
    CODE_CUE_POINT = "codeCuePoint.CodeCuePoint"
    ENTRY = "1"
    CATEGORY = "2"
    USER = "3"
    PARTNER = "4"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaMetadataOrderBy:
    CREATED_AT_ASC = "+createdAt"
    METADATA_PROFILE_VERSION_ASC = "+metadataProfileVersion"
    UPDATED_AT_ASC = "+updatedAt"
    VERSION_ASC = "+version"
    CREATED_AT_DESC = "-createdAt"
    METADATA_PROFILE_VERSION_DESC = "-metadataProfileVersion"
    UPDATED_AT_DESC = "-updatedAt"
    VERSION_DESC = "-version"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaMetadataProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package External
# @subpackage Kaltura
class KalturaMetadata(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            metadataProfileId=NotImplemented,
            metadataProfileVersion=NotImplemented,
            metadataObjectType=NotImplemented,
            objectId=NotImplemented,
            version=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            xml=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var int
        # @readonly
        self.metadataProfileId = metadataProfileId

        # @var int
        # @readonly
        self.metadataProfileVersion = metadataProfileVersion

        # @var KalturaMetadataObjectType
        # @readonly
        self.metadataObjectType = metadataObjectType

        # @var string
        # @readonly
        self.objectId = objectId

        # @var int
        # @readonly
        self.version = version

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var KalturaMetadataStatus
        # @readonly
        self.status = status

        # @var string
        # @readonly
        self.xml = xml


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'metadataProfileId': getXmlNodeInt, 
        'metadataProfileVersion': getXmlNodeInt, 
        'metadataObjectType': (KalturaEnumsFactory.createString, "KalturaMetadataObjectType"), 
        'objectId': getXmlNodeText, 
        'version': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaMetadataStatus"), 
        'xml': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadata.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadata")
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def getMetadataProfileVersion(self):
        return self.metadataProfileVersion

    def getMetadataObjectType(self):
        return self.metadataObjectType

    def getObjectId(self):
        return self.objectId

    def getVersion(self):
        return self.version

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getStatus(self):
        return self.status

    def getXml(self):
        return self.xml


# @package External
# @subpackage Kaltura
class KalturaMetadataListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMetadata
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMetadata), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


# @package External
# @subpackage Kaltura
class KalturaMetadataProfile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            metadataObjectType=NotImplemented,
            version=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            xsd=NotImplemented,
            views=NotImplemented,
            xslt=NotImplemented,
            createMode=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var KalturaMetadataObjectType
        self.metadataObjectType = metadataObjectType

        # @var int
        # @readonly
        self.version = version

        # @var string
        self.name = name

        # @var string
        self.systemName = systemName

        # @var string
        self.description = description

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var KalturaMetadataProfileStatus
        # @readonly
        self.status = status

        # @var string
        # @readonly
        self.xsd = xsd

        # @var string
        # @readonly
        self.views = views

        # @var string
        # @readonly
        self.xslt = xslt

        # @var KalturaMetadataProfileCreateMode
        self.createMode = createMode


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'metadataObjectType': (KalturaEnumsFactory.createString, "KalturaMetadataObjectType"), 
        'version': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaMetadataProfileStatus"), 
        'xsd': getXmlNodeText, 
        'views': getXmlNodeText, 
        'xslt': getXmlNodeText, 
        'createMode': (KalturaEnumsFactory.createInt, "KalturaMetadataProfileCreateMode"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfile")
        kparams.addStringEnumIfDefined("metadataObjectType", self.metadataObjectType)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntEnumIfDefined("createMode", self.createMode)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getMetadataObjectType(self):
        return self.metadataObjectType

    def setMetadataObjectType(self, newMetadataObjectType):
        self.metadataObjectType = newMetadataObjectType

    def getVersion(self):
        return self.version

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getStatus(self):
        return self.status

    def getXsd(self):
        return self.xsd

    def getViews(self):
        return self.views

    def getXslt(self):
        return self.xslt

    def getCreateMode(self):
        return self.createMode

    def setCreateMode(self, newCreateMode):
        self.createMode = newCreateMode


# @package External
# @subpackage Kaltura
class KalturaMetadataProfileField(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            xPath=NotImplemented,
            key=NotImplemented,
            label=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var string
        # @readonly
        self.xPath = xPath

        # @var string
        # @readonly
        self.key = key

        # @var string
        # @readonly
        self.label = label


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'xPath': getXmlNodeText, 
        'key': getXmlNodeText, 
        'label': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileField.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileField")
        return kparams

    def getId(self):
        return self.id

    def getXPath(self):
        return self.xPath

    def getKey(self):
        return self.key

    def getLabel(self):
        return self.label


# @package External
# @subpackage Kaltura
class KalturaMetadataProfileFieldListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMetadataProfileField
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMetadataProfileField), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileFieldListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileFieldListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


# @package External
# @subpackage Kaltura
class KalturaMetadataProfileListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMetadataProfile
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMetadataProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


# @package External
# @subpackage Kaltura
class KalturaImportMetadataJobData(KalturaJobData):
    def __init__(self,
            srcFileUrl=NotImplemented,
            destFileLocalPath=NotImplemented,
            metadataId=NotImplemented):
        KalturaJobData.__init__(self)

        # @var string
        self.srcFileUrl = srcFileUrl

        # @var string
        self.destFileLocalPath = destFileLocalPath

        # @var int
        self.metadataId = metadataId


    PROPERTY_LOADERS = {
        'srcFileUrl': getXmlNodeText, 
        'destFileLocalPath': getXmlNodeText, 
        'metadataId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaImportMetadataJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaJobData.toParams(self)
        kparams.put("objectType", "KalturaImportMetadataJobData")
        kparams.addStringIfDefined("srcFileUrl", self.srcFileUrl)
        kparams.addStringIfDefined("destFileLocalPath", self.destFileLocalPath)
        kparams.addIntIfDefined("metadataId", self.metadataId)
        return kparams

    def getSrcFileUrl(self):
        return self.srcFileUrl

    def setSrcFileUrl(self, newSrcFileUrl):
        self.srcFileUrl = newSrcFileUrl

    def getDestFileLocalPath(self):
        return self.destFileLocalPath

    def setDestFileLocalPath(self, newDestFileLocalPath):
        self.destFileLocalPath = newDestFileLocalPath

    def getMetadataId(self):
        return self.metadataId

    def setMetadataId(self, newMetadataId):
        self.metadataId = newMetadataId


# @package External
# @subpackage Kaltura
class KalturaMetadataBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            metadataProfileIdEqual=NotImplemented,
            metadataProfileVersionEqual=NotImplemented,
            metadataProfileVersionGreaterThanOrEqual=NotImplemented,
            metadataProfileVersionLessThanOrEqual=NotImplemented,
            metadataObjectTypeEqual=NotImplemented,
            objectIdEqual=NotImplemented,
            objectIdIn=NotImplemented,
            versionEqual=NotImplemented,
            versionGreaterThanOrEqual=NotImplemented,
            versionLessThanOrEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var int
        self.metadataProfileIdEqual = metadataProfileIdEqual

        # @var int
        self.metadataProfileVersionEqual = metadataProfileVersionEqual

        # @var int
        self.metadataProfileVersionGreaterThanOrEqual = metadataProfileVersionGreaterThanOrEqual

        # @var int
        self.metadataProfileVersionLessThanOrEqual = metadataProfileVersionLessThanOrEqual

        # @var KalturaMetadataObjectType
        self.metadataObjectTypeEqual = metadataObjectTypeEqual

        # @var string
        self.objectIdEqual = objectIdEqual

        # @var string
        self.objectIdIn = objectIdIn

        # @var int
        self.versionEqual = versionEqual

        # @var int
        self.versionGreaterThanOrEqual = versionGreaterThanOrEqual

        # @var int
        self.versionLessThanOrEqual = versionLessThanOrEqual

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var KalturaMetadataStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn


    PROPERTY_LOADERS = {
        'partnerIdEqual': getXmlNodeInt, 
        'metadataProfileIdEqual': getXmlNodeInt, 
        'metadataProfileVersionEqual': getXmlNodeInt, 
        'metadataProfileVersionGreaterThanOrEqual': getXmlNodeInt, 
        'metadataProfileVersionLessThanOrEqual': getXmlNodeInt, 
        'metadataObjectTypeEqual': (KalturaEnumsFactory.createString, "KalturaMetadataObjectType"), 
        'objectIdEqual': getXmlNodeText, 
        'objectIdIn': getXmlNodeText, 
        'versionEqual': getXmlNodeInt, 
        'versionGreaterThanOrEqual': getXmlNodeInt, 
        'versionLessThanOrEqual': getXmlNodeInt, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaMetadataStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaMetadataBaseFilter")
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addIntIfDefined("metadataProfileIdEqual", self.metadataProfileIdEqual)
        kparams.addIntIfDefined("metadataProfileVersionEqual", self.metadataProfileVersionEqual)
        kparams.addIntIfDefined("metadataProfileVersionGreaterThanOrEqual", self.metadataProfileVersionGreaterThanOrEqual)
        kparams.addIntIfDefined("metadataProfileVersionLessThanOrEqual", self.metadataProfileVersionLessThanOrEqual)
        kparams.addStringEnumIfDefined("metadataObjectTypeEqual", self.metadataObjectTypeEqual)
        kparams.addStringIfDefined("objectIdEqual", self.objectIdEqual)
        kparams.addStringIfDefined("objectIdIn", self.objectIdIn)
        kparams.addIntIfDefined("versionEqual", self.versionEqual)
        kparams.addIntIfDefined("versionGreaterThanOrEqual", self.versionGreaterThanOrEqual)
        kparams.addIntIfDefined("versionLessThanOrEqual", self.versionLessThanOrEqual)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        return kparams

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getMetadataProfileIdEqual(self):
        return self.metadataProfileIdEqual

    def setMetadataProfileIdEqual(self, newMetadataProfileIdEqual):
        self.metadataProfileIdEqual = newMetadataProfileIdEqual

    def getMetadataProfileVersionEqual(self):
        return self.metadataProfileVersionEqual

    def setMetadataProfileVersionEqual(self, newMetadataProfileVersionEqual):
        self.metadataProfileVersionEqual = newMetadataProfileVersionEqual

    def getMetadataProfileVersionGreaterThanOrEqual(self):
        return self.metadataProfileVersionGreaterThanOrEqual

    def setMetadataProfileVersionGreaterThanOrEqual(self, newMetadataProfileVersionGreaterThanOrEqual):
        self.metadataProfileVersionGreaterThanOrEqual = newMetadataProfileVersionGreaterThanOrEqual

    def getMetadataProfileVersionLessThanOrEqual(self):
        return self.metadataProfileVersionLessThanOrEqual

    def setMetadataProfileVersionLessThanOrEqual(self, newMetadataProfileVersionLessThanOrEqual):
        self.metadataProfileVersionLessThanOrEqual = newMetadataProfileVersionLessThanOrEqual

    def getMetadataObjectTypeEqual(self):
        return self.metadataObjectTypeEqual

    def setMetadataObjectTypeEqual(self, newMetadataObjectTypeEqual):
        self.metadataObjectTypeEqual = newMetadataObjectTypeEqual

    def getObjectIdEqual(self):
        return self.objectIdEqual

    def setObjectIdEqual(self, newObjectIdEqual):
        self.objectIdEqual = newObjectIdEqual

    def getObjectIdIn(self):
        return self.objectIdIn

    def setObjectIdIn(self, newObjectIdIn):
        self.objectIdIn = newObjectIdIn

    def getVersionEqual(self):
        return self.versionEqual

    def setVersionEqual(self, newVersionEqual):
        self.versionEqual = newVersionEqual

    def getVersionGreaterThanOrEqual(self):
        return self.versionGreaterThanOrEqual

    def setVersionGreaterThanOrEqual(self, newVersionGreaterThanOrEqual):
        self.versionGreaterThanOrEqual = newVersionGreaterThanOrEqual

    def getVersionLessThanOrEqual(self):
        return self.versionLessThanOrEqual

    def setVersionLessThanOrEqual(self, newVersionLessThanOrEqual):
        self.versionLessThanOrEqual = newVersionLessThanOrEqual

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


# @package External
# @subpackage Kaltura
class KalturaMetadataProfileBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            metadataObjectTypeEqual=NotImplemented,
            metadataObjectTypeIn=NotImplemented,
            versionEqual=NotImplemented,
            nameEqual=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createModeEqual=NotImplemented,
            createModeNotEqual=NotImplemented,
            createModeIn=NotImplemented,
            createModeNotIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var KalturaMetadataObjectType
        self.metadataObjectTypeEqual = metadataObjectTypeEqual

        # @var string
        self.metadataObjectTypeIn = metadataObjectTypeIn

        # @var int
        self.versionEqual = versionEqual

        # @var string
        self.nameEqual = nameEqual

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var KalturaMetadataProfileStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var KalturaMetadataProfileCreateMode
        self.createModeEqual = createModeEqual

        # @var KalturaMetadataProfileCreateMode
        self.createModeNotEqual = createModeNotEqual

        # @var string
        self.createModeIn = createModeIn

        # @var string
        self.createModeNotIn = createModeNotIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'metadataObjectTypeEqual': (KalturaEnumsFactory.createString, "KalturaMetadataObjectType"), 
        'metadataObjectTypeIn': getXmlNodeText, 
        'versionEqual': getXmlNodeInt, 
        'nameEqual': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaMetadataProfileStatus"), 
        'statusIn': getXmlNodeText, 
        'createModeEqual': (KalturaEnumsFactory.createInt, "KalturaMetadataProfileCreateMode"), 
        'createModeNotEqual': (KalturaEnumsFactory.createInt, "KalturaMetadataProfileCreateMode"), 
        'createModeIn': getXmlNodeText, 
        'createModeNotIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringEnumIfDefined("metadataObjectTypeEqual", self.metadataObjectTypeEqual)
        kparams.addStringIfDefined("metadataObjectTypeIn", self.metadataObjectTypeIn)
        kparams.addIntIfDefined("versionEqual", self.versionEqual)
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntEnumIfDefined("createModeEqual", self.createModeEqual)
        kparams.addIntEnumIfDefined("createModeNotEqual", self.createModeNotEqual)
        kparams.addStringIfDefined("createModeIn", self.createModeIn)
        kparams.addStringIfDefined("createModeNotIn", self.createModeNotIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getMetadataObjectTypeEqual(self):
        return self.metadataObjectTypeEqual

    def setMetadataObjectTypeEqual(self, newMetadataObjectTypeEqual):
        self.metadataObjectTypeEqual = newMetadataObjectTypeEqual

    def getMetadataObjectTypeIn(self):
        return self.metadataObjectTypeIn

    def setMetadataObjectTypeIn(self, newMetadataObjectTypeIn):
        self.metadataObjectTypeIn = newMetadataObjectTypeIn

    def getVersionEqual(self):
        return self.versionEqual

    def setVersionEqual(self, newVersionEqual):
        self.versionEqual = newVersionEqual

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getCreateModeEqual(self):
        return self.createModeEqual

    def setCreateModeEqual(self, newCreateModeEqual):
        self.createModeEqual = newCreateModeEqual

    def getCreateModeNotEqual(self):
        return self.createModeNotEqual

    def setCreateModeNotEqual(self, newCreateModeNotEqual):
        self.createModeNotEqual = newCreateModeNotEqual

    def getCreateModeIn(self):
        return self.createModeIn

    def setCreateModeIn(self, newCreateModeIn):
        self.createModeIn = newCreateModeIn

    def getCreateModeNotIn(self):
        return self.createModeNotIn

    def setCreateModeNotIn(self, newCreateModeNotIn):
        self.createModeNotIn = newCreateModeNotIn


# @package External
# @subpackage Kaltura
class KalturaTransformMetadataJobData(KalturaJobData):
    def __init__(self,
            srcXslPath=NotImplemented,
            srcVersion=NotImplemented,
            destVersion=NotImplemented,
            destXsdPath=NotImplemented,
            metadataProfileId=NotImplemented):
        KalturaJobData.__init__(self)

        # @var string
        self.srcXslPath = srcXslPath

        # @var int
        self.srcVersion = srcVersion

        # @var int
        self.destVersion = destVersion

        # @var string
        self.destXsdPath = destXsdPath

        # @var int
        self.metadataProfileId = metadataProfileId


    PROPERTY_LOADERS = {
        'srcXslPath': getXmlNodeText, 
        'srcVersion': getXmlNodeInt, 
        'destVersion': getXmlNodeInt, 
        'destXsdPath': getXmlNodeText, 
        'metadataProfileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTransformMetadataJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaJobData.toParams(self)
        kparams.put("objectType", "KalturaTransformMetadataJobData")
        kparams.addStringIfDefined("srcXslPath", self.srcXslPath)
        kparams.addIntIfDefined("srcVersion", self.srcVersion)
        kparams.addIntIfDefined("destVersion", self.destVersion)
        kparams.addStringIfDefined("destXsdPath", self.destXsdPath)
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        return kparams

    def getSrcXslPath(self):
        return self.srcXslPath

    def setSrcXslPath(self, newSrcXslPath):
        self.srcXslPath = newSrcXslPath

    def getSrcVersion(self):
        return self.srcVersion

    def setSrcVersion(self, newSrcVersion):
        self.srcVersion = newSrcVersion

    def getDestVersion(self):
        return self.destVersion

    def setDestVersion(self, newDestVersion):
        self.destVersion = newDestVersion

    def getDestXsdPath(self):
        return self.destXsdPath

    def setDestXsdPath(self, newDestXsdPath):
        self.destXsdPath = newDestXsdPath

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId


# @package External
# @subpackage Kaltura
class KalturaCompareMetadataCondition(KalturaCompareCondition):
    def __init__(self,
            type=NotImplemented,
            not_=NotImplemented,
            value=NotImplemented,
            comparison=NotImplemented,
            xPath=NotImplemented,
            profileId=NotImplemented):
        KalturaCompareCondition.__init__(self,
            type,
            not_,
            value,
            comparison)

        # May contain the full xpath to the field in three formats
        # 	 1. Slashed xPath, e.g. /metadata/myElementName
        # 	 2. Using local-name function, e.g. /[local-name()='metadata']/[local-name()='myElementName']
        # 	 3. Using only the field name, e.g. myElementName, it will be searched as //myElementName
        # @var string
        self.xPath = xPath

        # Metadata profile id
        # @var int
        self.profileId = profileId


    PROPERTY_LOADERS = {
        'xPath': getXmlNodeText, 
        'profileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaCompareCondition.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCompareMetadataCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCompareCondition.toParams(self)
        kparams.put("objectType", "KalturaCompareMetadataCondition")
        kparams.addStringIfDefined("xPath", self.xPath)
        kparams.addIntIfDefined("profileId", self.profileId)
        return kparams

    def getXPath(self):
        return self.xPath

    def setXPath(self, newXPath):
        self.xPath = newXPath

    def getProfileId(self):
        return self.profileId

    def setProfileId(self, newProfileId):
        self.profileId = newProfileId


# @package External
# @subpackage Kaltura
class KalturaMatchMetadataCondition(KalturaMatchCondition):
    def __init__(self,
            type=NotImplemented,
            not_=NotImplemented,
            values=NotImplemented,
            xPath=NotImplemented,
            profileId=NotImplemented):
        KalturaMatchCondition.__init__(self,
            type,
            not_,
            values)

        # May contain the full xpath to the field in three formats
        # 	 1. Slashed xPath, e.g. /metadata/myElementName
        # 	 2. Using local-name function, e.g. /[local-name()='metadata']/[local-name()='myElementName']
        # 	 3. Using only the field name, e.g. myElementName, it will be searched as //myElementName
        # @var string
        self.xPath = xPath

        # Metadata profile id
        # @var int
        self.profileId = profileId


    PROPERTY_LOADERS = {
        'xPath': getXmlNodeText, 
        'profileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaMatchCondition.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMatchMetadataCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMatchCondition.toParams(self)
        kparams.put("objectType", "KalturaMatchMetadataCondition")
        kparams.addStringIfDefined("xPath", self.xPath)
        kparams.addIntIfDefined("profileId", self.profileId)
        return kparams

    def getXPath(self):
        return self.xPath

    def setXPath(self, newXPath):
        self.xPath = newXPath

    def getProfileId(self):
        return self.profileId

    def setProfileId(self, newProfileId):
        self.profileId = newProfileId


# @package External
# @subpackage Kaltura
class KalturaMetadataFilter(KalturaMetadataBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            metadataProfileIdEqual=NotImplemented,
            metadataProfileVersionEqual=NotImplemented,
            metadataProfileVersionGreaterThanOrEqual=NotImplemented,
            metadataProfileVersionLessThanOrEqual=NotImplemented,
            metadataObjectTypeEqual=NotImplemented,
            objectIdEqual=NotImplemented,
            objectIdIn=NotImplemented,
            versionEqual=NotImplemented,
            versionGreaterThanOrEqual=NotImplemented,
            versionLessThanOrEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaMetadataBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            partnerIdEqual,
            metadataProfileIdEqual,
            metadataProfileVersionEqual,
            metadataProfileVersionGreaterThanOrEqual,
            metadataProfileVersionLessThanOrEqual,
            metadataObjectTypeEqual,
            objectIdEqual,
            objectIdIn,
            versionEqual,
            versionGreaterThanOrEqual,
            versionLessThanOrEqual,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMetadataBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMetadataBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMetadataFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaMetadataProfileFilter(KalturaMetadataProfileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            metadataObjectTypeEqual=NotImplemented,
            metadataObjectTypeIn=NotImplemented,
            versionEqual=NotImplemented,
            nameEqual=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createModeEqual=NotImplemented,
            createModeNotEqual=NotImplemented,
            createModeIn=NotImplemented,
            createModeNotIn=NotImplemented):
        KalturaMetadataProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            partnerIdEqual,
            metadataObjectTypeEqual,
            metadataObjectTypeIn,
            versionEqual,
            nameEqual,
            systemNameEqual,
            systemNameIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            createModeEqual,
            createModeNotEqual,
            createModeIn,
            createModeNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMetadataProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMetadataProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaMetadataSearchItem(KalturaSearchOperator):
    def __init__(self,
            type=NotImplemented,
            items=NotImplemented,
            metadataProfileId=NotImplemented,
            orderBy=NotImplemented):
        KalturaSearchOperator.__init__(self,
            type,
            items)

        # @var int
        self.metadataProfileId = metadataProfileId

        # @var string
        self.orderBy = orderBy


    PROPERTY_LOADERS = {
        'metadataProfileId': getXmlNodeInt, 
        'orderBy': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSearchOperator.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataSearchItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchOperator.toParams(self)
        kparams.put("objectType", "KalturaMetadataSearchItem")
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addStringIfDefined("orderBy", self.orderBy)
        return kparams

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy


########## services ##########

# @package External
# @subpackage Kaltura
class KalturaMetadataService(KalturaServiceBase):
    """Metadata service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, metadataProfileId, objectType, objectId, xmlData):
        """Allows you to add a metadata object and metadata content associated with Kaltura object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("metadataProfileId", metadataProfileId);
        kparams.addStringIfDefined("objectType", objectType)
        kparams.addStringIfDefined("objectId", objectId)
        kparams.addStringIfDefined("xmlData", xmlData)
        self.client.queueServiceActionCall("metadata_metadata", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def addFromFile(self, metadataProfileId, objectType, objectId, xmlFile):
        """Allows you to add a metadata object and metadata file associated with Kaltura object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("metadataProfileId", metadataProfileId);
        kparams.addStringIfDefined("objectType", objectType)
        kparams.addStringIfDefined("objectId", objectId)
        kfiles = KalturaFiles()
        kfiles.put("xmlFile", xmlFile);
        self.client.queueServiceActionCall("metadata_metadata", "addFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def addFromUrl(self, metadataProfileId, objectType, objectId, url):
        """Allows you to add a metadata xml data from remote URL"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("metadataProfileId", metadataProfileId);
        kparams.addStringIfDefined("objectType", objectType)
        kparams.addStringIfDefined("objectId", objectId)
        kparams.addStringIfDefined("url", url)
        self.client.queueServiceActionCall("metadata_metadata", "addFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def addFromBulk(self, metadataProfileId, objectType, objectId, url):
        """Allows you to add a metadata xml data from remote URL.
        	 Enables different permissions than addFromUrl action."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("metadataProfileId", metadataProfileId);
        kparams.addStringIfDefined("objectType", objectType)
        kparams.addStringIfDefined("objectId", objectId)
        kparams.addStringIfDefined("url", url)
        self.client.queueServiceActionCall("metadata_metadata", "addFromBulk", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def get(self, id):
        """Retrieve a metadata object by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("metadata_metadata", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def update(self, id, xmlData = NotImplemented, version = NotImplemented):
        """Update an existing metadata object with new XML content"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addStringIfDefined("xmlData", xmlData)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("metadata_metadata", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def updateFromFile(self, id, xmlFile = NotImplemented):
        """Update an existing metadata object with new XML file"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kfiles = KalturaFiles()
        kfiles.put("xmlFile", xmlFile);
        self.client.queueServiceActionCall("metadata_metadata", "updateFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List metadata objects by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("metadata_metadata", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataListResponse)

    def delete(self, id):
        """Delete an existing metadata"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("metadata_metadata", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def invalidate(self, id, version = NotImplemented):
        """Mark existing metadata as invalid
        	 Used by batch metadata transform"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("metadata_metadata", "invalidate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def serve(self, id):
        """Serves metadata XML file"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall('metadata_metadata', 'serve', kparams)
        return self.client.getServeUrl()

    def updateFromXSL(self, id, xslFile):
        """Action transforms current metadata object XML using a provided XSL."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kfiles = KalturaFiles()
        kfiles.put("xslFile", xslFile);
        self.client.queueServiceActionCall("metadata_metadata", "updateFromXSL", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)


# @package External
# @subpackage Kaltura
class KalturaMetadataProfileService(KalturaServiceBase):
    """Metadata Profile service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, metadataProfile, xsdData, viewsData = NotImplemented):
        """Allows you to add a metadata profile object and metadata profile content associated with Kaltura object type"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("metadataProfile", metadataProfile)
        kparams.addStringIfDefined("xsdData", xsdData)
        kparams.addStringIfDefined("viewsData", viewsData)
        self.client.queueServiceActionCall("metadata_metadataprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def addFromFile(self, metadataProfile, xsdFile, viewsFile = NotImplemented):
        """Allows you to add a metadata profile object and metadata profile file associated with Kaltura object type"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("metadataProfile", metadataProfile)
        kfiles = KalturaFiles()
        kfiles.put("xsdFile", xsdFile);
        kfiles.put("viewsFile", viewsFile);
        self.client.queueServiceActionCall("metadata_metadataprofile", "addFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def get(self, id):
        """Retrieve a metadata profile object by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("metadata_metadataprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def update(self, id, metadataProfile, xsdData = NotImplemented, viewsData = NotImplemented):
        """Update an existing metadata object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("metadataProfile", metadataProfile)
        kparams.addStringIfDefined("xsdData", xsdData)
        kparams.addStringIfDefined("viewsData", viewsData)
        self.client.queueServiceActionCall("metadata_metadataprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List metadata profile objects by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("metadata_metadataprofile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfileListResponse)

    def listFields(self, metadataProfileId):
        """List metadata profile fields by metadata profile id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("metadataProfileId", metadataProfileId);
        self.client.queueServiceActionCall("metadata_metadataprofile", "listFields", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfileFieldListResponse)

    def delete(self, id):
        """Delete an existing metadata profile"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("metadata_metadataprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def revert(self, id, toVersion):
        """Update an existing metadata object definition file"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("toVersion", toVersion);
        self.client.queueServiceActionCall("metadata_metadataprofile", "revert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def updateDefinitionFromFile(self, id, xsdFile):
        """Update an existing metadata object definition file"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kfiles = KalturaFiles()
        kfiles.put("xsdFile", xsdFile);
        self.client.queueServiceActionCall("metadata_metadataprofile", "updateDefinitionFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def updateViewsFromFile(self, id, viewsFile):
        """Update an existing metadata object views file"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kfiles = KalturaFiles()
        kfiles.put("viewsFile", viewsFile);
        self.client.queueServiceActionCall("metadata_metadataprofile", "updateViewsFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def updateTransformationFromFile(self, id, xsltFile):
        """Update an existing metadata object xslt file"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kfiles = KalturaFiles()
        kfiles.put("xsltFile", xsltFile);
        self.client.queueServiceActionCall("metadata_metadataprofile", "updateTransformationFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def serve(self, id):
        """Serves metadata profile XSD file"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall('metadata_metadataprofile', 'serve', kparams)
        return self.client.getServeUrl()

    def serveView(self, id):
        """Serves metadata profile view file"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall('metadata_metadataprofile', 'serveView', kparams)
        return self.client.getServeUrl()

########## main ##########
class KalturaMetadataClientPlugin(KalturaClientPlugin):
    # KalturaMetadataClientPlugin
    instance = None

    # @return KalturaMetadataClientPlugin
    @staticmethod
    def get():
        if KalturaMetadataClientPlugin.instance == None:
            KalturaMetadataClientPlugin.instance = KalturaMetadataClientPlugin()
        return KalturaMetadataClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'metadata': KalturaMetadataService,
            'metadataProfile': KalturaMetadataProfileService,
        }

    def getEnums(self):
        return {
            'KalturaMetadataProfileCreateMode': KalturaMetadataProfileCreateMode,
            'KalturaMetadataProfileStatus': KalturaMetadataProfileStatus,
            'KalturaMetadataStatus': KalturaMetadataStatus,
            'KalturaMetadataObjectType': KalturaMetadataObjectType,
            'KalturaMetadataOrderBy': KalturaMetadataOrderBy,
            'KalturaMetadataProfileOrderBy': KalturaMetadataProfileOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaMetadata': KalturaMetadata,
            'KalturaMetadataListResponse': KalturaMetadataListResponse,
            'KalturaMetadataProfile': KalturaMetadataProfile,
            'KalturaMetadataProfileField': KalturaMetadataProfileField,
            'KalturaMetadataProfileFieldListResponse': KalturaMetadataProfileFieldListResponse,
            'KalturaMetadataProfileListResponse': KalturaMetadataProfileListResponse,
            'KalturaImportMetadataJobData': KalturaImportMetadataJobData,
            'KalturaMetadataBaseFilter': KalturaMetadataBaseFilter,
            'KalturaMetadataProfileBaseFilter': KalturaMetadataProfileBaseFilter,
            'KalturaTransformMetadataJobData': KalturaTransformMetadataJobData,
            'KalturaCompareMetadataCondition': KalturaCompareMetadataCondition,
            'KalturaMatchMetadataCondition': KalturaMatchMetadataCondition,
            'KalturaMetadataFilter': KalturaMetadataFilter,
            'KalturaMetadataProfileFilter': KalturaMetadataProfileFilter,
            'KalturaMetadataSearchItem': KalturaMetadataSearchItem,
        }

    # @return string
    def getName(self):
        return 'metadata'

