from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel

from cms_blocks.models import LinkBlock, BodyRichTextBlock, BodyImageBlock  # Import blocks from cms_blocks


class HomePage(Page):
    subheader = models.CharField(max_length=255, blank=True)
    intro = RichTextField(blank=True)
    links = StreamField([("link", LinkBlock())], use_json_field=True, blank=True)
    body_content = StreamField([
        ("richtext", BodyRichTextBlock()),
        ("image", BodyImageBlock()),
    ], use_json_field=True, blank=True)
    footer = RichTextField(blank=True)  # Footer content

    content_panels = Page.content_panels + [
        FieldPanel("subheader"),
        FieldPanel("intro"),
        FieldPanel("links"),
        FieldPanel("body_content"),
        FieldPanel("footer"),
    ]


    template = "home/home_page.html"