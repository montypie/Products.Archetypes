from AccessControl import ClassSecurityInfo
from Products.CMFCore import CMFCorePermissions
from ArchetypeTool import registerType, process_types, listTypes

from BaseContent import BaseContent
from BaseFolder import BaseFolder
from BaseBTreeFolder import BaseBTreeFolder
from OrderedBaseFolder import OrderedBaseFolder

from ExtensibleMetadata import ExtensibleMetadata

from Schema import Schema, MetadataSchema
from Field  import *
from Widget import *
from Storage import *

from utils import DisplayList

BaseBTreeFolderSchema = BaseBTreeFolder.schema

BaseFolderSchema = BaseFolder.schema

BaseSchema = BaseContent.schema

I18NCONTENT_ACTIONS = ({ 'id': 'translate',
                       'name': 'Translate',
                       'action': 'portal_form/base_translation',
                       'permissions': (CMFCorePermissions.ModifyPortalContent,),
                       },
                     { 'id': 'translations',
                       'name': 'Translations',
                       'action': 'portal_form/manage_translations_form',
                       'permissions': (CMFCorePermissions.ModifyPortalContent,),
                       },
                     )

