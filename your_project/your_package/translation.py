from modeltranslation.translator import translator, TranslationOptions
from your_package.models import Profile

class ProfileTranslationOptions(TranslationOptions):
	fields = ('description',)

translator.register( Profile, ProfileTranslationOptions )
