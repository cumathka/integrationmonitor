from wagtail.blocks import CharBlock, StructBlock, RichTextBlock, URLBlock
from wagtail.blocks import PageChooserBlock
from wagtail.images.blocks import ImageBlock

# Custom block for the links
class LinkBlock(StructBlock):
    title = CharBlock(required=True)
    icon = CharBlock(required=False, help_text="e.g. 'fa-solid fa-briefcase'")
    page = PageChooserBlock(required=False)
    external_url = URLBlock(required=False)

    class Meta:
        template = "blocks/link_block.html"
        icon = "link"
        label = "Link Block"

# Standard RichText block for body content
class BodyRichTextBlock(RichTextBlock):
    class Meta:
        icon = "doc-full"
        label = "Rich Text"

# Standard Image block for body content
class BodyImageBlock(ImageBlock):
    class Meta:
        icon = "image"
        label = "Image"
