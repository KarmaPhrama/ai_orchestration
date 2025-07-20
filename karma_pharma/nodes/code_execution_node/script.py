import requests
import json

# video would be video uri
def main(
    post_text: str,
    image_url: str = None,
) -> str:
    # access token valid for 2 months
    ACCESS_TOKEN = "AQXw9V_DVejVpjmXDg_va4dbvqHwCmbb1wLxgH8jp5S558XIIguNXJ8J2C_hxEXKWvTtANzG_0iJIr1X-t640d4R7tn0pFypjsNGQcR0SbCdPq4BCaKRZbEY2klrgR3S7FkgMMZQLv0B4IWdy6O4i78JGX5gVQOMabZyh7u_jDEJcaDzkopbHN1xyA1Aya1C82NtWNytLpijqDXaeiEjaHXFgyK6NT8blQmu5wYk6Fs-Nr3GNWi8mLxsRo4Mj4I_l-_NzjpQOvhApD_sLrbDs43in4Glu9jCDU-h_AaD8_xPDhn0AIlzM4pxSpJaMasuFuGg2mf8XrIt1e_0utGAKDqD5Ou7RQ"
    # sub of the user
    SUB_VALUE = "CCxNdWV4d3"
    api_url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    image_urn = None
    if (image_url):
        image_post_data = {
            "registerUploadRequest": {
                "recipes": [
                    "urn:li:digitalmediaRecipe:feedshare-image"
                ],
                "owner": f"urn:li:person:{SUB_VALUE}",
                "serviceRelationships": [
                    {
                        "relationshipType": "OWNER",
                        "identifier": "urn:li:userGeneratedContent"
                    }
                ]
            }
        }
        try:
            response = requests.post("https://api.linkedin.com/v2/assets?action=registerUpload", headers=headers, data=json.dumps(image_post_data))
            response.raise_for_status()
            res_image_data = response.json()
            upload_url, image_urn = res_image_data.get("value").get("uploadMechanism").get("com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest").get("uploadUrl"), res_image_data.get("value").get("asset").split(":")[-1]
            image_res = requests.get(image_url, timeout=15)
            image_res.raise_for_status()
            image_binary_data = get_response.content
            image_content_type = get_response.headers.get('Content-Type', 'application/octet-stream')
            specific_headers = {
                'Authorization': f'Bearer {ACCESS_TOKEN}',
                'Content-Type': image_content_type
            }
            put_response = requests.put(
                upload_url,
                headers=specific_headers,
                data=image_binary_data,
                timeout=30
            )
            put_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return f"❌ An error occurred in image upload: {e}"
    post_data = None
    if image_url and image_urn:
        post_data = {
            "author": PERSON_URN,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_text
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": "Main Image"
                            },
                            "media": f"urn:li:digitalmediaAsset:{image_urn}",
                            "title": {
                                "text": "Main Image Text"
                            }
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
    else:
        post_data = {
            "author": PERSON_URN,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_text
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(post_data))
        response.raise_for_status()
        return f"✅ Success! Post was created. Status Code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error occured: {e}"
