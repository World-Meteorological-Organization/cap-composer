# Generated by Django 4.2.16 on 2025-03-10 17:57

import cap_composer.capeditor.blocks
from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0027_capalertlistpage_alerts_infos_per_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capalertpage',
            name='info',
            field=wagtail.fields.StreamField([('alert_info', 44)], block_lookup={0: ('wagtail.blocks.ChoiceBlock', [], {'choices': cap_composer.capeditor.blocks.get_hazard_types, 'help_text': 'The text denoting the type of the subject event of the alert message. You can define hazards events monitored by your institution from CAP settings', 'label': 'Event'}), 1: ('wagtail.blocks.ChoiceBlock', [], {'choices': cap_composer.capeditor.blocks.get_language_choices, 'help_text': "The code denoting the language of the alert message.If not selected, 'en-US' will be used as default", 'label': 'Language', 'required': False}), 2: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('Immediate', 'Immediate - Responsive action SHOULD be taken immediately'), ('Expected', 'Expected - Responsive action SHOULD be taken soon (within next hour)'), ('Future', 'Future - Responsive action SHOULD be taken in the near future'), ('Past', 'Past - Responsive action is no longer required')], 'help_text': 'The code denoting the urgency of the subject event of the alert message', 'label': 'Urgency'}), 3: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('Extreme', 'Extreme - Extraordinary threat to life or property'), ('Severe', 'Severe - Significant threat to life or property'), ('Moderate', 'Moderate - Possible threat to life or property'), ('Minor', 'Minor - Minimal to no known threat to life or property')], 'help_text': 'The code denoting the severity of the subject event of the alert message', 'label': 'Severity'}), 4: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('Observed', 'Observed - Determined to have occurred or to be ongoing'), ('Likely', 'Likely - Likely (percentage > ~50%)'), ('Possible', 'Possible - Possible but not likely (percentage <= ~50%)'), ('Unlikely', 'Unlikely - Not expected to occur (percentage ~ 0)')], 'help_text': 'The code denoting the certainty of the subject event of the alert message', 'label': 'Certainty'}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'The text headline of the alert message. Make it direct and actionable as possible while remaining short', 'label': 'Headline', 'max_length': 160, 'required': False}), 6: ('wagtail.blocks.TextBlock', (), {'help_text': 'The text describing the subject event of the alert message. An extended description of the hazard or event that occasioned this message', 'label': 'Description', 'required': True}), 7: ('wagtail.blocks.TextBlock', (), {'help_text': 'The text describing the recommended action to be taken by recipients of the alert message', 'label': 'Instruction', 'required': False}), 8: ('wagtail.blocks.DateTimeBlock', (), {'help_text': 'The effective time of the information of the alert message. If not set, the sent date will be used', 'label': 'Effective', 'required': False}), 9: ('wagtail.blocks.DateTimeBlock', (), {'help_text': 'The expected time of the beginning of the subject event of the alert message', 'label': 'Onset', 'required': False}), 10: ('wagtail.blocks.DateTimeBlock', (), {'help_text': 'The expiry time of the information of the alert message. If not set, each recipient is free to set its own policy as to when the message is no longer in effect.', 'label': 'Expires', 'required': True}), 11: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('Shelter', 'Shelter - Take shelter in place or per instruction'), ('Evacuate', 'Evacuate - Relocate as instructed in the instruction'), ('Prepare', 'Prepare - Relocate as instructed in the instruction'), ('Execute', 'Execute - Execute a pre-planned activity identified in instruction'), ('Avoid', 'Avoid - Avoid the subject event as per the instruction'), ('Monitor', 'Monitor - Attend to information sources as described in instruction'), ('Assess', 'Assess - Evaluate the information in this message - DONT USE FOR PUBLIC ALERTS'), ('AllClear', 'All Clear - The subject event no longer poses a threat or concern and any follow on action is described in instruction'), ('None', 'No action recommended')], 'help_text': 'The code denoting the type of action recommended for the target audience', 'label': 'Response type'}), 12: ('wagtail.blocks.StructBlock', [[('response_type', 11)]], {'label': 'Response Type'}), 13: ('wagtail.blocks.ListBlock', (12,), {'default': [], 'label': 'Response Types'}), 14: ('wagtail.blocks.CharBlock', (), {'help_text': 'The human-readable name of the agency or authority issuing this alert.', 'label': 'Sender name', 'max_length': 255, 'required': False}), 15: ('wagtail.blocks.CharBlock', (), {'help_text': 'The text describing the contact for follow-up and confirmation of the alert message', 'label': 'Contact', 'max_length': 255, 'required': False}), 16: ('wagtail.blocks.TextBlock', (), {'help_text': 'The text describing the intended audience of the alert message', 'label': 'Audience', 'required': False}), 17: ('wagtail.blocks.TextBlock', (), {'help_text': 'The text describing the affected area of the alert message', 'label': 'Affected areas / Regions'}), 18: ('wagtail.blocks.ChoiceBlock', [], {'choices': [(0, 'Level 0'), (1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')], 'label': 'Administrative Level'}), 19: ('cap_composer.capeditor.blocks.BoundaryFieldBlock', (), {'help_text': 'The paired values of points defining a polygon that delineates the affected area of the alert message', 'label': 'Boundary'}), 20: ('wagtail.blocks.CharBlock', (), {'help_text': 'The specific or minimum altitude of the affected area of the alert message', 'label': 'Altitude', 'max_length': 100, 'required': False}), 21: ('wagtail.blocks.CharBlock', (), {'help_text': 'The maximum altitude of the affected area of the alert message.MUST NOT be used except in combination with the altitude element. ', 'label': 'Ceiling', 'max_length': 100, 'required': False}), 22: ('wagtail.blocks.TextBlock', (), {'help_text': 'User-assigned string designating the domain of the code. Acronyms SHOULD be represented in all capital letters without periods (e.g., SAME, FIPS, ZIP', 'label': 'Value Name'}), 23: ('wagtail.blocks.TextBlock', (), {'help_text': 'A string (which may represent a number) denoting the value itself', 'label': 'Value'}), 24: ('wagtail.blocks.StructBlock', [[('valueName', 22), ('value', 23)]], {'label': 'Geocode', 'required': False}), 25: ('wagtail.blocks.ListBlock', (24,), {'default': []}), 26: ('wagtail.blocks.StructBlock', [[('areaDesc', 17), ('admin_level', 18), ('boundary', 19), ('altitude', 20), ('ceiling', 21), ('geocode', 25)]], {'label': 'Admin Boundary'}), 27: ('cap_composer.capeditor.blocks.PolygonOrMultiPolygonFieldBlock', (), {'help_text': 'The paired values of points defining a polygon that delineates the affected area of the alert message', 'label': 'Polygon'}), 28: ('wagtail.blocks.StructBlock', [[('areaDesc', 17), ('polygon', 27), ('altitude', 20), ('ceiling', 21), ('geocode', 25)]], {'label': 'Draw Polygon'}), 29: ('cap_composer.capeditor.blocks.CircleFieldBlock', (), {'help_text': 'Drag the marker to change position', 'label': 'Circle'}), 30: ('wagtail.blocks.StructBlock', [[('areaDesc', 17), ('circle', 29), ('altitude', 20), ('ceiling', 21), ('geocode', 25)]], {'label': 'Circle'}), 31: ('wagtailmodelchooser.blocks.ModelChooserBlock', (), {'label': 'Area', 'target_model': 'capeditor.predefinedalertarea'}), 32: ('wagtail.blocks.StructBlock', [[('area', 31), ('altitude', 20), ('ceiling', 21), ('geocode', 25)]], {'label': 'Predefined Area'}), 33: ('wagtail.blocks.StreamBlock', [[('boundary_block', 26), ('polygon_block', 28), ('circle_block', 30), ('predefined_block', 32)]], {'help_text': 'Admin Boundary, Polygon, Circle, or Predefined area', 'label': 'Alert Area'}), 34: ('wagtail.blocks.TextBlock', (), {'help_text': 'The text describing the type and content of the resource file', 'label': 'Resource Description'}), 35: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 36: ('wagtail.blocks.StructBlock', [[('resourceDesc', 34), ('file', 35)]], {}), 37: ('wagtail.blocks.URLBlock', (), {'help_text': 'Link to external resource. This can be for example a link to related websites. ', 'verbose_name': 'External Resource Link'}), 38: ('wagtail.blocks.StructBlock', [[('resourceDesc', 34), ('external_url', 37)]], {}), 39: ('wagtail.blocks.StreamBlock', [[('file_resource', 36), ('external_resource', 38)]], {'help_text': 'Additional file with supplemental information related to this alert information', 'label': 'Resources', 'required': False}), 40: ('wagtail.blocks.TextBlock', (), {'label': 'Name'}), 41: ('wagtail.blocks.TextBlock', (), {'label': 'Value'}), 42: ('wagtail.blocks.StructBlock', [[('valueName', 40), ('value', 41)]], {'label': 'Parameter'}), 43: ('wagtail.blocks.ListBlock', (42,), {'default': [], 'label': 'Parameters'}), 44: ('wagtail.blocks.StructBlock', [[('event', 0), ('language', 1), ('urgency', 2), ('severity', 3), ('certainty', 4), ('headline', 5), ('description', 6), ('instruction', 7), ('effective', 8), ('onset', 9), ('expires', 10), ('responseType', 13), ('senderName', 14), ('contact', 15), ('audience', 16), ('area', 33), ('resource', 39), ('parameter', 43)]], {'label': 'Alert Information'})}, verbose_name='Alert Information'),
        ),
    ]
