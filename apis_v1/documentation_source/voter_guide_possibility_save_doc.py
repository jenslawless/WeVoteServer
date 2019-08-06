# apis_v1/documentation_source/voter_guide_possibility_save_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def voter_guide_possibility_save_doc_template_values(url_root):
    """
    Show documentation about voterGuidePossibilitySave
    """
    required_query_parameter_list = [
        {
            'name':         'voter_device_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'An 88 character unique identifier linked to a voter record on the server',
        },
        {
            'name':         'api_key',
            'value':        'string (from post, cookie, or get (in that order))',  # boolean, integer, long, string
            'description':  'The unique key provided to any organization using the WeVoteServer APIs',
        },
        {
            'name':         'voter_guide_possibility_id',
            'value':        'integer',  # boolean, integer, long, string
            'description':  'The id of the voterGuidePossibility to be saved.',
        },
    ]
    optional_query_parameter_list = [
        {
            'name':         'candidates_missing_from_we_vote',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'Are there candidates endorsed on this page that we do not have in our Candidate table?',
        },
        {
            'name':         'capture_detailed_comments',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'Are there comments that go along with endorsements that remain to be captured?',
        },
        {
            'name':         'clear_organization_options',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'Is the organization this endorsement linked to incorrect, that should be unlinked?',
        },
        {
            'name':         'contributor_comments',
            'value':        'string',  # boolean, integer, long, string
            'description':  'Comments from the person saving this VoterGuidePossibility.',
        },
        {
            'name':         'contributor_email',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The email address (unverified) of the person submitting this VoterGuidePossibility.',
        },
        {
            'name':         'hide_from_active_review',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'We are done reviewing and processing this VoterGuidePossibility.',
        },
        {
            'name':         'ignore_this_source',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'This web page does not have endorsements and should be ignored.',
        },
        {
            'name':         'internal_notes',
            'value':        'string',  # boolean, integer, long, string
            'description':  'Internal notes from a We Vote political data manager.',
        },
        {
            'name':         'organization_we_vote_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The we_vote_id of the organization making these endorsements.',
        },
        {
            'name':         'possible_organization_name',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The name of the organization making these endorsements, '
                            'for possible matching with organization in We Vote database.',
        },
        {
            'name':         'limit_to_this_state_code',
            'value':        'string',  # boolean, integer, long, string
            'description':  'All of these endorsements relate to candidates or ballot items in this state.',
        },
        {
            'name':         'possible_organization_twitter_handle',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The Twitter handle of the organization making these endorsements, '
                            'for possible matching with organization in We Vote database.',
        },
    ]

    potential_status_codes_list = [
        {
            'code':         'VALID_VOTER_DEVICE_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_device_id parameter was not included.',
        },
        {
            'code':         'VALID_VOTER_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_id was not found.',
        },
        {
            'code':         'VOTER_GUIDE_POSSIBILITY_SAVED',
            'description':  'URL saved.',
        },
    ]

    try_now_link_variables_dict = {
        'voter_guide_possibility_id': '8',
    }

    api_response = '{\n' \
                   '  "status": string,\n' \
                   '  "success": boolean,\n' \
                   '  "candidate": dict\n' \
                   '   {\n' \
                   '     "candidate_we_vote_id": string,\n' \
                   '     "candidate_name": string,\n' \
                   '     "candidate_website": string,\n' \
                   '     "candidate_twitter_handle": string,\n' \
                   '     "candidate_email": string,\n' \
                   '     "candidate_facebook": string,\n' \
                   '     "we_vote_hosted_profile_image_url_medium": string,\n'\
                   '     "we_vote_hosted_profile_image_url_tiny": string,\n' \
                   '   },\n' \
                   '  "candidates_missing_from_we_vote": boolean,\n' \
                   '  "cannot_find_endorsements": boolean,\n' \
                   '  "capture_detailed_comments": boolean,\n' \
                   '  "contributor_comments": string,\n' \
                   '  "contributor_email": string,\n' \
                   '  "hide_from_active_review": boolean,\n' \
                   '  "ignore_this_source": boolean,\n' \
                   '  "internal_notes": string,\n' \
                   '  "organization": dict\n' \
                   '   {\n' \
                   '     "organization_we_vote_id": string,\n' \
                   '     "organization_name": string,\n' \
                   '     "organization_website": string,\n' \
                   '     "organization_twitter_handle": string,\n' \
                   '     "organization_email": string,\n' \
                   '     "organization_facebook": string,\n' \
                   '     "we_vote_hosted_profile_image_url_medium": string,\n'\
                   '     "we_vote_hosted_profile_image_url_tiny": string,\n' \
                   '   },\n' \
                   '  "possible_candidate_name": string,\n' \
                   '  "possible_candidate_twitter_handle": string,\n' \
                   '  "possible_organization_name": string,\n' \
                   '  "possible_organization_twitter_handle": string,\n' \
                   '  "limit_to_this_state_code": string,\n' \
                   '  "url_to_scan": string,\n' \
                   '  "voter_device_id": string (88 characters long),\n' \
                   '  "voter_guide_possibility_edit": string,\n' \
                   '  "voter_guide_possibility_id": integer,\n' \
                   '  "voter_guide_possibility_type": string,\n' \
                   '}'

    template_values = {
        'api_name': 'voterGuidePossibilitySave',
        'api_slug': 'voterGuidePossibilitySave',
        'api_introduction':
            "Update existing VoterGuidePossibility with altered data.",
        'try_now_link': 'apis_v1:voterGuidePossibilitySaveView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
