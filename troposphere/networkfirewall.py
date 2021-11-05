# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 25.0.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import boolean, integer

VALID_RULE_GROUP_TYPES = ("STATEFUL", "STATELESS")


def validate_rule_group_type(rule_group_type):
    """Validate Type for RuleGroup"""
    if rule_group_type not in VALID_RULE_GROUP_TYPES:
        raise ValueError(
            "RuleGroup Type must be one of %s" % ", ".join(VALID_RULE_GROUP_TYPES)
        )
    return rule_group_type


class SubnetMapping(AWSProperty):
    props = {
        "SubnetId": (str, True),
    }


class Firewall(AWSObject):
    resource_type = "AWS::NetworkFirewall::Firewall"

    props = {
        "DeleteProtection": (boolean, False),
        "Description": (str, False),
        "FirewallName": (str, True),
        "FirewallPolicyArn": (str, True),
        "FirewallPolicyChangeProtection": (boolean, False),
        "SubnetChangeProtection": (boolean, False),
        "SubnetMappings": ([SubnetMapping], True),
        "Tags": (Tags, False),
        "VpcId": (str, True),
    }


class Dimension(AWSProperty):
    props = {
        "Value": (str, True),
    }


class PublishMetricAction(AWSProperty):
    props = {
        "Dimensions": ([Dimension], True),
    }


class ActionDefinition(AWSProperty):
    props = {
        "PublishMetricAction": (PublishMetricAction, False),
    }


class CustomAction(AWSProperty):
    props = {
        "ActionDefinition": (ActionDefinition, True),
        "ActionName": (str, True),
    }


class StatefulEngineOptions(AWSProperty):
    props = {
        "RuleOrder": (str, False),
    }


class StatefulRuleGroupReference(AWSProperty):
    props = {
        "Priority": (integer, False),
        "ResourceArn": (str, True),
    }


class StatelessRuleGroupReference(AWSProperty):
    props = {
        "Priority": (integer, True),
        "ResourceArn": (str, True),
    }


class FirewallPolicyProperty(AWSProperty):
    props = {
        "StatefulDefaultActions": ([str], False),
        "StatefulEngineOptions": (StatefulEngineOptions, False),
        "StatefulRuleGroupReferences": ([StatefulRuleGroupReference], False),
        "StatelessCustomActions": ([CustomAction], False),
        "StatelessDefaultActions": ([str], True),
        "StatelessFragmentDefaultActions": ([str], True),
        "StatelessRuleGroupReferences": ([StatelessRuleGroupReference], False),
    }


class FirewallPolicy(AWSObject):
    resource_type = "AWS::NetworkFirewall::FirewallPolicy"

    props = {
        "Description": (str, False),
        "FirewallPolicy": (FirewallPolicyProperty, True),
        "FirewallPolicyName": (str, True),
        "Tags": (Tags, False),
    }


class LogDestinationConfig(AWSProperty):
    props = {
        "LogDestination": (dict, True),
        "LogDestinationType": (str, True),
        "LogType": (str, True),
    }


class LoggingConfiguration(AWSProperty):
    props = {
        "LogDestinationConfigs": ([LogDestinationConfig], True),
    }


class RuleVariables(AWSProperty):
    props = {
        "IPSets": (dict, False),
        "PortSets": (dict, False),
    }


class RulesSourceList(AWSProperty):
    props = {
        "GeneratedRulesType": (str, True),
        "TargetTypes": ([str], True),
        "Targets": ([str], True),
    }


class Header(AWSProperty):
    props = {
        "Destination": (str, True),
        "DestinationPort": (str, True),
        "Direction": (str, True),
        "Protocol": (str, True),
        "Source": (str, True),
        "SourcePort": (str, True),
    }


class RuleOption(AWSProperty):
    props = {
        "Keyword": (str, True),
        "Settings": ([str], False),
    }


class StatefulRule(AWSProperty):
    props = {
        "Action": (str, True),
        "Header": (Header, True),
        "RuleOptions": ([RuleOption], True),
    }


class Address(AWSProperty):
    props = {
        "AddressDefinition": (str, True),
    }


class PortRange(AWSProperty):
    props = {
        "FromPort": (integer, True),
        "ToPort": (integer, True),
    }


class TCPFlagField(AWSProperty):
    props = {
        "Flags": ([str], True),
        "Masks": ([str], False),
    }


class MatchAttributes(AWSProperty):
    props = {
        "DestinationPorts": ([PortRange], False),
        "Destinations": ([Address], False),
        "Protocols": ([integer], False),
        "SourcePorts": ([PortRange], False),
        "Sources": ([Address], False),
        "TCPFlags": ([TCPFlagField], False),
    }


class RuleDefinition(AWSProperty):
    props = {
        "Actions": ([str], True),
        "MatchAttributes": (MatchAttributes, True),
    }


class StatelessRule(AWSProperty):
    props = {
        "Priority": (integer, True),
        "RuleDefinition": (RuleDefinition, True),
    }


class StatelessRulesAndCustomActions(AWSProperty):
    props = {
        "CustomActions": ([CustomAction], False),
        "StatelessRules": ([StatelessRule], True),
    }


class RulesSource(AWSProperty):
    props = {
        "RulesSourceList": (RulesSourceList, False),
        "RulesString": (str, False),
        "StatefulRules": ([StatefulRule], False),
        "StatelessRulesAndCustomActions": (StatelessRulesAndCustomActions, False),
    }


class StatefulRuleOptions(AWSProperty):
    props = {
        "RuleOrder": (str, False),
    }


class RuleGroupProperty(AWSProperty):
    props = {
        "RuleVariables": (RuleVariables, False),
        "RulesSource": (RulesSource, True),
        "StatefulRuleOptions": (StatefulRuleOptions, False),
    }


class RuleGroup(AWSObject):
    resource_type = "AWS::NetworkFirewall::RuleGroup"

    props = {
        "Capacity": (integer, True),
        "Description": (str, False),
        "RuleGroup": (RuleGroupProperty, False),
        "RuleGroupName": (str, True),
        "Tags": (Tags, False),
        "Type": (validate_rule_group_type, True),
    }
