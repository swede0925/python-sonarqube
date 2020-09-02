#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PROJECT_PULL_REQUESTS_DELETE_ENDPOINT,
    API_PROJECT_PULL_REQUESTS_LIST_ENDPOINT
)


class SonarQubepRrojectPullRequests:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def search_project_pull_requests(self, project):
        """
        List the pull requests of a project.

        :param project: Project key
        :return:
        """
        params = {
            'project': project
        }
        resp = self.sonarqube.make_call('get', API_PROJECT_PULL_REQUESTS_LIST_ENDPOINT, **params)
        return resp.json()

    def delete_project_pull_requests(self, project, pull_request_id):
        """
        Delete a pull request.

        :param project: Project key
        :param pull_request_id: Pull request id
        :return:
        """
        params = {
            'project': project,
            'pullRequest': pull_request_id
        }
        self.sonarqube.make_call('post', API_PROJECT_PULL_REQUESTS_DELETE_ENDPOINT, **params)
